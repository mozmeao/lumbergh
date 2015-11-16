from django.conf import settings
from django.http import HttpResponse


def robots(request):
    action = 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow'
    return HttpResponse('User-agent: *\n{}: /'.format(action), content_type='text/plain')
