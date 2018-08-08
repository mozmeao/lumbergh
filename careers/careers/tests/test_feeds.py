# -*- coding: utf-8 -*-
from django.urls import reverse

from careers.base.tests import TestCase
from careers.careers.tests import PositionFactory


class FeedTests(TestCase):
    def test_career_feed(self):
        job_id_1 = 'oflWVfwb'
        job_id_2 = 'oFlWVfwB'
        job_1 = PositionFactory.create(job_id=job_id_1)
        job_2 = PositionFactory.create(job_id=job_id_2)

        url = reverse('careers.feed')
        response = self.client.get(url)
        self.assertEqual(response['Content-Type'],
                         'application/rss+xml; charset=utf-8')
        self.assertEqual(response.status_code, 200)

        content = response.content.decode('utf-8')
        self.assertIn(reverse('careers.listings'), content)
        self.assertIn(url, content)

        for job in [job_1, job_2]:
            self.assertIn(job.title, content)
            self.assertIn(job.description, content)
            self.assertIn(job.department, content)
            self.assertIn(job.get_absolute_url(), content)
