from unittest.mock import mock_open, patch

from careers.base.tests import TestCase
from careers.university import utils


EVENTS = """
- name: Summer Party 1
  location: Beach House
  end_date: 2017-04-22

- name: Summer Party 2
  location: Beach House
  start_date: 2017-04-20

- location: Beach House 3
  start_date: 2017-04-20
  end_date: 2017-04-22

- name: Beach House 4
  start_date: 2017-04-20
  end_date: 2017-04-22

- name: Autumn Party!
  location: Forest Cabin
  start_date: 2017-09-20
  end_date: 2017-09-22

- name: Summer Party!
  location: Beach House
  start_date: 2017-06-20
  end_date: 2017-06-22

- name: Summer Party 5
  location: Beach House
  start_date: 2017-04-20
  end_date: 2017-04-19
"""


class LoadEventsTests(TestCase):
    def test_base(self):
        m = mock_open(read_data=EVENTS)
        with patch.object(utils, 'open', m, create=True):
            events = utils.load_events()

        assert(len(events) == 2)
        assert(events[0]['name'] == 'Summer Party!')
        assert(events[1]['name'] == 'Autumn Party!')

    def test_with_real_file(self):
        events = utils.load_events()
        assert(isinstance(events, list))
