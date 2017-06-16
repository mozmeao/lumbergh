import json
import logging

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from raven.contrib.django.models import client

from careers.careers.models import Position


def robots(request):
    action = 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow'
    return HttpResponse('User-agent: *\n{}: /'.format(action), content_type='text/plain')


def healthz(request):
    """For use with Healthchecks."""
    assert Position.objects.exists(), "No positions exist"
    return HttpResponse('OK')


@csrf_exempt
@require_POST
def csp_violation_capture(request):
    data = client.get_data_from_request(request)
    data.update({
        'level': logging.INFO,
        'logger': 'CSP',
    })
    try:
        csp_data = json.loads(request.body)
    except ValueError:
        # Cannot decode CSP violation data, ignore
        return HttpResponseBadRequest('Invalid CSP Report')

    try:
        blocked_uri = csp_data['csp-report']['blocked-uri']
    except KeyError:
        # Incomplete CSP report
        return HttpResponseBadRequest('Incomplete CSP Report')

    client.captureMessage(
        message='CSP Violation: {}'.format(blocked_uri),
        data=data)

    return HttpResponse('Captured CSP violation, thanks for reporting.')
