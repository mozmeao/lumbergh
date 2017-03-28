import locale
from datetime import date

from careers.base.tests import TestCase
from careers.university.templatetags.helpers import format_event_date

MAY = locale.nl_langinfo(locale.ABMON_5)
JUN = locale.nl_langinfo(locale.ABMON_6)


class FormatEventDateTests(TestCase):
    def test_date_no_end_date(self):
        """If the event has no end date, just display the start date."""
        event = {'name': '1', 'location': 'example',
                 'start_date': date(2012, 5, 5), 'end_date': date(2012, 5, 5)}
        self.assertEqual(format_event_date(event),
                         '{may} 5, 2012'.format(may=MAY))

    def test_date_same_month(self):
        """If the event starts and ends in the same month, display a shortened date."""
        event = {'name': '1', 'location': 'example',
                 'start_date': date(2012, 5, 5), 'end_date': date(2012, 5, 9)}
        self.assertEqual(format_event_date(event),
                         '{may} 5-9, 2012'.format(may=MAY))

    def test_date_different_months(self):
        """If the event starts in one month and ends in another, show both dates."""
        event = {'name': '1', 'location': 'example',
                 'start_date': date(2012, 5, 5), 'end_date': date(2012, 6, 9)}
        self.assertEqual(format_event_date(event),
                         '{may} 5, 2012 - {jun} 9, 2012'.format(may=MAY, jun=JUN))
