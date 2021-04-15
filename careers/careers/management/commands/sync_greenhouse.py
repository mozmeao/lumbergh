# -*- coding: utf-8 -*-
import html
import re

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

import bleach
import requests
from html5lib.filters.base import Filter

from careers.careers.models import Position

GREENHOUSE_URL = 'https://api.greenhouse.io/v1/boards/{}/jobs/?content=true'

ALLOWED_TAGS = [
    'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em',
    'i', 'li', 'ol', 'ul', 'p', 'br', 'h1', 'h2', 'h3', 'h4',
    'strong',
]


class HeaderConverterFilter(Filter):
    def __iter__(self):
        for token in Filter.__iter__(self):
            if (token['type'] in ['StartTag', 'EndTag']):
                if token['name'] in ['h1', 'h2', 'h3']:
                    token['name'] = 'h4'
            yield token


cleaner = bleach.sanitizer.Cleaner(tags=ALLOWED_TAGS, strip=True, filters=[HeaderConverterFilter])


class Command(BaseCommand):
    args = '(no args)'
    help = 'Sync jobs from Greenhouse'

    @transaction.atomic
    def handle(self, *args, **options):
        jobs_added = 0
        jobs_updated = 0
        jobs_removed = 0
        job_ids = []

        response = requests.get(GREENHOUSE_URL.format(settings.GREENHOUSE_BOARD_TOKEN))
        response.raise_for_status()

        data = response.json()
        for job in data['jobs']:
            # Maybe GH sometimes includes jobs with the same ID multiple times
            # in the json. Capture the event in Sentry and look the other way.
            if job['id'] in job_ids:
                continue

            job_ids.append(job['id'])

            job_object, created = (Position.objects
                                   .get_or_create(job_id=job['id'], source='gh'))

            departments = job.get('departments', '')
            if departments:
                department = departments[0]['name'] or ''
            else:
                department = ''

            is_mofo = False
            if department == 'Mozilla Foundation':
                is_mofo = True

            offices = job.get('offices', '')
            if offices:
                location = ','.join([office['name'] for office in offices])
            else:
                location = ''

            jobLocations = job.get('location', {}).get('name', '')

            description = html.unescape(job.get('content', ''))
            description = cleaner.clean(description)
            # Remove empty paragraphs and h4s and paragraphs with \xa0
            # (no-brake space). I ♥ regex
            description = re.sub(r'<(p|h4)>([ ]*|(\xa0)+)</(p|h4)>', '', description)

            for metadata in job.get('metadata', []):
                if metadata.get('name', '') == 'Employment Type':
                    position_type = metadata['value'] or ''
                    break
            else:
                position_type = ''

            object_data = {
                'title': job['title'],
                'department': department,
                'is_mofo': is_mofo,
                'location': location,
                'job_locations': jobLocations,
                'description': description,
                'position_type': position_type,
                'apply_url': job['absolute_url'],
                'updated_at': job['updated_at'],
            }

            changed = False
            for key, value in object_data.items():
                if getattr(job_object, key, None) != value:
                    changed = True
                    setattr(job_object, key, value)

            if changed:
                if created:
                    jobs_added += 1
                else:
                    jobs_updated += 1
                job_object.save()

        positions_to_be_removed = Position.objects.exclude(job_id__in=job_ids, source='gh')
        jobs_removed = positions_to_be_removed.count()
        positions_to_be_removed.delete()

        self.stdout.write(
            'Jobs added: {added} updated: {updated} '
            'removed: {removed}'.format(added=jobs_added,
                                        updated=jobs_updated,
                                        removed=jobs_removed))
