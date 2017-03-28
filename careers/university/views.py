from datetime import date

from django.shortcuts import render

from careers.careers.models import Position
from careers.university import EVENTS, utils


def index(request):
    today = date.today()

    param = request.GET.get('open_for_applications')
    open_for_applications = 'true'

    if param:
        open_for_applications = param == 'true'
    else:
        open_for_applications = Position.objects.filter(position_type='Intern').exists()

    return render(request, 'university/index.jinja', {
        'events': utils.filter_events(EVENTS, today),
        'open_for_applications': open_for_applications,
    })
