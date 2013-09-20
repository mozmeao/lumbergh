import locale
from datetime import date

from django.core.exceptions import ValidationError

from nose.tools import assert_raises, eq_

from careers.base.tests import TestCase
from careers.university.tests import EventFactory


MAY = locale.nl_langinfo(locale.ABMON_5)
JUN = locale.nl_langinfo(locale.ABMON_6)


class EventTests(TestCase):
    def test_date_no_end_date(self):
        """If the event has no end date, just display the start date."""
        event = EventFactory.build(start_date=date(2012, 5, 5))
        eq_(event.date, '{may} 5, 2012'.format(may=MAY))

    def test_date_same_month(self):
        """If the event starts and ends in the same month, display a shortened date."""
        event = EventFactory.build(start_date=date(2012, 5, 5), end_date=date(2012, 5, 9))
        eq_(event.date, '{may} 5-9, 2012'.format(may=MAY))

    def test_date_different_months(self):
        """If the event starts in one month and ends in another, show both dates."""
        event = EventFactory.build(start_date=date(2012, 5, 5), end_date=date(2012, 6, 9))
        eq_(event.date, '{may} 5, 2012 - {jun} 9, 2012'.format(may=MAY, jun=JUN))

    def test_clean_invalid_end_date(self):
        """
        If an event's end date is on or before its start date, clean should raise a
        ValidationError.
        """
        event = EventFactory.build(start_date=date(2011, 1, 1), end_date=date(2010, 1, 1))
        with assert_raises(ValidationError):
            event.clean()

        event = EventFactory.build(start_date=date(2010, 1, 1), end_date=date(2010, 1, 1))
        with assert_raises(ValidationError):
            event.clean()

    def test_clean_valid_end_date(self):
        """
        If an event's end date is after its start date or doesn't exist, clean should not raise a
        ValidationError.
        """
        event = EventFactory.build(start_date=date(2011, 1, 1), end_date=date(2013, 1, 1))
        event.clean()

        event = EventFactory.build(start_date=date(2011, 1, 1), end_date=None)
        event.clean()

    def test_unicode(self):
        event = EventFactory.build(start_date=date(2011, 5, 5), name='Foo', location='Bar')
        eq_(unicode(event), u'Foo, Bar - {may} 5, 2011'.format(may=MAY))
