from datetime import date

from django.db.models import Q
from django.shortcuts import render

from django_jobvite.models import Position

from careers.university.models import Event


def index(request):
    today = date.today()
    date_filter = Q(start_date__gte=today) | Q(end_date__isnull=False, end_date__gte=today)

    param = request.GET.get('open_for_applications')
    if param:
        open_for_applications = param == 'true'
    else:
        open_for_applications = Position.objects.filter(job_type='Intern').exists()

    return render(request, 'university/index.html', {
        'events': Event.objects.filter(date_filter).order_by('start_date'),
        'open_for_applications': open_for_applications,
    })
