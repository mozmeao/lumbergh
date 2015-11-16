from datetime import date

from django.test.client import RequestFactory

from django_jobvite.models import Position
from mock import patch

from careers.base.tests import TestCase
from careers.careers.tests import PositionFactory as JobvitePositionFactory
from careers.university import views
from careers.university.tests import EventFactory


class IndexTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def _index(self, **kwargs):
        with patch('careers.university.views.render') as render:
            response = views.index(self.factory.get('/', kwargs))
            context = render.call_args[0][2]
        return response, context

    def test_event_filter(self):
        """
        The events shown on the university page should be limited to
        events occurring on or after the current date, and should be
        ordered by start date.
        """
        event1 = EventFactory.create(start_date=date(2010, 1, 6))
        event2 = EventFactory.create(start_date=date(2010, 2, 4))
        event3 = EventFactory.create(start_date=date(2010, 1, 3), end_date=date(2010, 1, 8))
        event4 = EventFactory.create(start_date=date(2010, 1, 2), end_date=date(2010, 1, 6))

        # Events that shouldn't be included.
        EventFactory.create(start_date=date(2010, 1, 2))
        EventFactory.create(start_date=date(2010, 1, 2), end_date=date(2010, 1, 5))

        with patch('careers.university.views.date') as mock_date:
            mock_date.today.return_value = date(2010, 1, 6)
            response, context = self._index()

        self.assertEqual(list(context['events']), [event4, event3, event1, event2])

    def test_open_for_applications(self):
        """
        If there are positions in the Intern category,
        open_for_applications should be True.
        """
        JobvitePositionFactory.create(job_type='Intern')
        response, context = self._index()
        self.assertTrue(context['open_for_applications'])

    def test_closed_for_applications(self):
        """
        If there aren't any positions in the Intern category,
        open_for_applications should be False.
        """
        self.assertEqual(Position.objects.count(), 0)
        response, context = self._index()
        self.assertTrue(not context['open_for_applications'])

    def test_open_for_applications_param(self):
        """
        If the open_for_applications GET parameter is set to 'true',
        open_for_applications should be True, even if there are no
        intern positions.
        """
        self.assertEqual(Position.objects.count(), 0)
        response, context = self._index(open_for_applications='true')
        self.assertTrue(context['open_for_applications'])

    def test_closed_for_applications_param(self):
        """
        If the open_for_applications GET parameter is set to 'false',
        open_for_applications should be False, even if there are intern
        positions.
        """
        JobvitePositionFactory.create(job_type='Intern')
        response, context = self._index(open_for_applications='false')
        self.assertTrue(not context['open_for_applications'])
