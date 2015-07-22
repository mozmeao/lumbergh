from collections import defaultdict

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import bleach
import requests

from careers.django_workable.models import Category, Position


FIELD_MAP = {
    'shortcode': 'shortcode',
    'title': 'title',
    'shortlink': 'detail_url',
    'application_url': 'apply_url',
    'full_description': 'description',
}

WORK_TYPE_MAP = {
    'Full-time': 'Regular (Full-Time)',
    'Part-time': 'Regular (Part-Time)',
    'Contract': 'Fixed-Term (MoFo)',
}


class Command(BaseCommand):
    help = 'Fetch job listings from Workable'

    def handle(self, *args, **options):
        if not getattr(settings, 'WORKABLE_URI', ''):
            raise CommandError('You must setup WORKABLE_URI in settings first.')

        if not getattr(settings, 'WORKABLE_API_KEY', ''):
            raise CommandError('You must setup WORKABLE_API_KEY too.')

        stats = defaultdict(lambda: 0)
        saved_positions = []
        headers = {'Authorization': 'Bearer {0}'.format(settings.WORKABLE_API_KEY)}
        jobs_response = requests.get(settings.WORKABLE_URI, headers=headers)
        jobs = jobs_response.json().get('jobs', [])

        for job in jobs:

            if job['state'] != 'published':
                continue

            job_data = requests.get(
                '{0}{1}'.format(settings.WORKABLE_URI, job['shortcode']),
                headers=headers)
            job_data = job_data.json()

            try:
                position = Position.objects.get(shortcode=job['shortcode'])
                stats['updated_positions'] += 1
            except Position.DoesNotExist:
                position = Position()
                stats['new_positions'] += 1

            for remote_field, local_field in FIELD_MAP.items():
                setattr(position, local_field, job_data[remote_field])

            position.job_type = WORK_TYPE_MAP.get(job_data['employment_type'],
                                                  job_data['employment_type'])

            # If telecommute is on, add Remote
            position.location = job_data['location']['city']
            if job_data['location']['telecommuting']:
                position.location += ', Remote'

            # Everything workable is Mozilla Foundation for now.
            category, created = Category.objects.get_or_create(name='Mozilla Foundation')
            position.category = category

            # Bleach description
            position.description = bleach.clean(position.description,
                                                tags=bleach.ALLOWED_TAGS + ['br', 'p'],
                                                strip=True)

            position.save()
            saved_positions.append(position.shortcode)

        # Remove expired positions
        stats['removed_positions'] = Position.objects.exclude(shortcode__in=saved_positions).count()
        Position.objects.exclude(shortcode__in=saved_positions).delete()
        stats['removed_categories'] = Category.objects.filter(position__isnull=True).count()
        Category.objects.filter(position__isnull=True).delete()


        print ' -> Added:                        {0}'.format(stats['new_positions'])
        print ' -> Updated:                      {0}'.format(stats['updated_positions'])
        print ' -> Removed:                      {0}'.format(stats['removed_positions'])
        print ' -> Removed Categories:           {0}'.format(stats['removed_categories'])
        print ' -> Total Workable.com positions: {0}'.format(Position.objects.all().count())
