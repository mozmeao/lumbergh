from django.core.urlresolvers import reverse

from careers.base.tests import TestCase


class HealthzViewTests(TestCase):
    def test_ok(self):
        response = self.client.get(reverse('watchman.ping'))
        self.assertEqual(response.status_code, 200)
