from datetime import date

from django.test.client import RequestFactory

from mock import patch
from nose.tools import eq_

from careers.base.tests import TestCase
from careers.university import views
from careers.university.tests import EventFactory


class IndexTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_event_filter(self):
        """
        The events shown on the university page should be limited to events occurring on or after
        the current date, and should be ordered by start date.
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

            with patch('careers.university.views.render') as render:
                response = views.index(self.factory.get('/'))

        eq_(response,  render.return_value)
        context = render.call_args[0][2]
        eq_(list(context['events']), [event4, event3, event1, event2])
