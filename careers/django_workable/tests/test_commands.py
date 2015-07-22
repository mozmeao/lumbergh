from mock import patch
from nose.tools import eq_

from django.conf import settings
from django.core.management.base import CommandError
from django.test.utils import override_settings

from careers.base.tests import TestCase
from careers.django_workable.management.commands import syncworkable
from careers.django_workable.models import Category, Position
from careers.django_workable.tests import CategoryFactory, PositionFactory


@override_settings(WORKABLE_URI='https://workable.example.com',
                   WORKABLE_API_KEY='secret')
class TestSyncWorkableCommand(TestCase):
    def setUp(self):
        self.command = syncworkable.Command()
        self.spec = 'careers.django_workable.management.commands.syncworkable.requests'

    @override_settings(WORKABLE_URI=None)
    def test_settings_workable_uri_does_not_exist(self):
        with self.assertRaises(CommandError):
            self.command.handle()

    @override_settings(WORKABLE_API_KEY=None)
    def test_settings_workable_api_key_does_not_exist(self):
        with self.assertRaises(CommandError):
            self.command.handle()

    def test_unpublished_jobs_are_ignored(self):
        data = {'jobs': [{'state': 'unpublished'}]}
        with patch(self.spec) as requests_mock:
            requests_mock.get().json().get().return_value = data
            self.command.handle()
        eq_(requests_mock.get.call_count, 2)

    def test_new_job_added(self):
        data = {'jobs': [{'state': 'published', 'shortcode': 'foo'}]}
        position_data = {'employment_type': 'type',
                         'shortcode': 'foo',
                         'title': 'title',
                         'shortlink': 'http://foo.bar',
                         'location': {'city': 'Paradise', 'telecommuting': True},
                         'application_url': 'http://example.com',
                         'full_description': '<h3>title</h3> test'}

        with patch(self.spec) as requests_mock:
            requests_mock.get().json.side_effect = [data, position_data]
            self.command.handle()

        eq_(requests_mock.get.call_count, 3)
        position = Position.objects.get(shortcode='foo')
        eq_(position.job_type, 'type')
        eq_(position.title, 'title')
        eq_(position.detail_url, 'http://foo.bar')
        eq_(position.apply_url, 'http://example.com')
        eq_(position.location, 'Paradise, Remote')
        eq_(position.description, 'title test')

        eq_(Position.objects.all().count(), 1)

    def test_existing_job_gets_updated(self):
        category = CategoryFactory.create(name='test category')
        PositionFactory.create(shortcode='foo', category=category)
        data = {'jobs': [{'state': 'published', 'shortcode': 'foo'}]}
        position_data = {'employment_type': 'type',
                         'shortcode': 'foo',
                         'title': 'title',
                         'shortlink': 'http://foo.bar',
                         'location': {'city': 'Paradise', 'telecommuting': True},
                         'application_url': 'http://example.com',
                         'full_description': '<h3>title</h3> test'}

        with patch(self.spec) as requests_mock:
            requests_mock.get().json.side_effect = [data, position_data]

            self.command.handle()

        eq_(requests_mock.get.call_count, 3)
        position = Position.objects.get(shortcode='foo')
        eq_(position.job_type, 'type')
        eq_(position.title, 'title')
        eq_(position.detail_url, 'http://foo.bar')
        eq_(position.apply_url, 'http://example.com')
        eq_(position.location, 'Paradise, Remote')
        eq_(position.description, 'title test')

        eq_(Position.objects.all().count(), 1)
        eq_(Category.objects.all().count(), 1)
        eq_(Category.objects.all()[0].name, 'Mozilla Foundation')

    def test_known_job_type_converted(self):
        data = {'jobs': [{'state': 'published', 'shortcode': 'foo'}]}
        position_data = {'employment_type': 'foo',
                         'shortcode': 'foo',
                         'title': 'title',
                         'shortlink': 'http://foo.bar',
                         'location': {'city': 'Paradise', 'telecommuting': True},
                         'application_url': 'http://example.com',
                         'full_description': '<h3>title</h3> test'}

        work_type_map_spec = 'careers.django_workable.management.commands.syncworkable.WORK_TYPE_MAP'
        with patch(work_type_map_spec, {'foo': 'bar'}):
            with patch(self.spec) as requests_mock:
                requests_mock.get().json.side_effect = [data, position_data]
                self.command.handle()
        position = Position.objects.get(shortcode='foo')
        eq_(position.job_type, 'bar')
