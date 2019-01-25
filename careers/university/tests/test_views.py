from django.urls import reverse

from careers.base.tests import TestCase
from careers.careers.models import Position
from careers.careers.tests import PositionFactory


class IndexTests(TestCase):
    def _index(self, params={}):
        url = reverse('university.index')
        response = self.client.get(url, params, follow=True)
        return response, response.context_data

    def test_open_for_applications(self):
        """
        If there are positions in the Intern category,
        open_for_applications should be True.
        """
        PositionFactory.create(position_type='Intern')
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
        response, context = self._index({'open_for_applications': 'true'})
        self.assertTrue(context['open_for_applications'])

    def test_closed_for_applications_param(self):
        """
        If the open_for_applications GET parameter is set to 'false',
        open_for_applications should be False, even if there are intern
        positions.
        """
        PositionFactory.create(position_type='Intern')
        response, context = self._index({'open_for_applications': 'false'})
        self.assertTrue(not context['open_for_applications'])
