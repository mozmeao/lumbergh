from django.conf import settings
from django.test import TestCase

from funfactory.urlresolvers import reverse
from nose.tools import eq_
from pyquery import PyQuery as pq

from django_jobvite.models import Category, Position


class CareersTest(TestCase):
    """Tests static pages for careers"""
    fixtures = ['django_jobvite.json']

    def test_homepage(self):
        """
        Test that homepage exists and
        categories and their positions
        also exist.
        """
        r = self.client.get(reverse('careers.home'), follow=True)
        eq_(r.status_code, 200)

        doc = pq(r.content)
        assert doc('.role-group.large ul')
        assert doc('.role-group.large ul li')
    
    def test_position_detail(self):
        """
        Test that the position page contains
        a job description and an apply button
        """
        position = Position.objects.filter(pk=1)
        url = reverse('careers.position', kwargs={'job_id': position[0].job_id})
        r = self.client.get(url, follow=True)
        eq_(r.status_code, 200)

        doc = pq(r.content)
        eq_('http://hire.jobvite.com/CompanyJobs/Apply.aspx?c=qpX9Vfwa&j=oPVSVfwh',
            doc.find('#job-apply').attr('href'))
