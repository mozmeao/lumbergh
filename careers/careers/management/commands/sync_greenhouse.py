import HTMLParser

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

import bleach
import requests

from careers.careers.models import Position

GREENHOUSE_URL = 'https://api.greenhouse.io/v1/boards/{}/jobs/?content=true'
H = HTMLParser.HTMLParser()


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
            job_ids.append(job['id'])

            job_object, created = (Position.objects
                                   .get_or_create(job_id=job['id'], source='gh'))

            departments = job.get('departments', '')
            if departments:
                department = departments[0]['name'] or ''
            else:
                department = ''

            offices = job.get('offices', '')
            if offices:
                location = ','.join([office['name'] for office in offices])
            else:
                location = ''

            description = H.unescape(job.get('content', ''))
            description = bleach.clean(description,
                                       tags=bleach.ALLOWED_TAGS + ['p', 'br'],
                                       strip=True)

            for metadata in job.get('metadata', []):
                if metadata.get('name', '') == 'Employment Type':
                    position_type = metadata['value'] or ''
                    break
            else:
                position_type = ''

            object_data = {
                'title': job['title'],
                'department': department,
                'location': location,
                'description': description,
                'position_type': position_type,
                'apply_url': job['absolute_url'],
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
