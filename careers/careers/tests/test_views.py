from funfactory.urlresolvers import reverse
from nose.tools import eq_

from careers.base.tests import TestCase
from careers.careers.tests import PositionFactory


class CareersTest(TestCase):
    """Tests static pages for careers"""
    def test_position_case_sensitive_match(self):
        """
        Validate that a position match is returned from a case-sensitive job id and it doesn't
        raise a multiple records error.
        """
        job_id_1 = 'oflWVfwb'
        job_id_2 = 'oFlWVfwB'
        PositionFactory.create(job_id=job_id_1)
        PositionFactory.create(job_id=job_id_2)

        url = reverse('careers.position', kwargs={'job_id': job_id_1})
        response = self.client.get(url, follow=True)
        eq_(response.status_code, 200)
        eq_(response.context['position'].job_id, job_id_1)

        url = reverse('careers.position', kwargs={'job_id': job_id_2})
        response = self.client.get(url, follow=True)
        eq_(response.status_code, 200)
        eq_(response.context['position'].job_id, job_id_2)
