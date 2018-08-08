from datetime import date

from django.urls import reverse
from mock import patch

from careers.base.tests import TestCase
from careers.careers.models import Position
from careers.careers.tests import PositionFactory


class IndexTests(TestCase):
    def _index(self, params={}):
        url = reverse('university.index')
        response = self.client.get(url, params, follow=True)
        return response, response.context_data

    def test_event_filter(self):
        """
        The events shown on the university page should be limited to
        events occurring on or after the current date, and should be
        ordered by start date.
        """
        event1 = {'name': '1', 'location': 'example',
                  'start_date': date(2010, 1, 2), 'end_date': date(2010, 1, 6)}
        event2 = {'name': '2', 'location': 'example',
                  'start_date': date(2010, 1, 3), 'end_date': date(2010, 1, 8)}
        event3 = {'name': '3', 'location': 'example',
                  'start_date': date(2010, 1, 6), 'end_date': date(2010, 1, 6)}
        event4 = {'name': '4', 'location': 'example',
                  'start_date': date(2010, 2, 4), 'end_date': date(2010, 2, 4)}

        with patch('careers.university.views.EVENTS', new_callable=list) as events:
            events.extend([
                event1, event2, event3, event4,
                # Events that shouldn't be included in page.
                {'name': '5', 'location': 'example',
                 'start_date': date(2010, 1, 2), 'end_date': date(2010, 1, 2)},
                {'name': '6', 'location': 'example',
                 'start_date': date(2010, 1, 2), 'end_date': date(2010, 1, 5)}
            ])

            with patch('careers.university.views.date') as mock_date:
                mock_date.today.return_value = date(2010, 1, 6)
                response, context = self._index()

        self.assertEqual(list(context['events']), [event1,  event2, event3, event4])

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
