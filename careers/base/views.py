from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def robots(request):
    action = 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow'
    return HttpResponse('User-agent: *\n{}: /'.format(action), content_type='text/plain')


def custom_404(request, exception=None):
    status = 404 if exception else 200
    return render(request, '404.jinja', status=status)
