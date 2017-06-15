from django.core.urlresolvers import reverse

from careers.base.tests import TestCase
from careers.careers.tests import PositionFactory


class HealthzViewTests(TestCase):
    def test_ok(self):
        PositionFactory.create()
        response = self.client.get(reverse('healthz'))
        self.assertEqual(response.status_code, 200)

    def test_fail(self):
        with self.assertRaises(AssertionError):
            self.client.get(reverse('healthz'))
