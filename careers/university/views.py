from datetime import date

from django.db.models import Q
from django.shortcuts import render

from careers.university.models import Event


def index(request):
    today = date.today()
    date_filter = Q(start_date__gte=today) | Q(end_date__isnull=False, end_date__gte=today)
    return render(request, 'university/index.html', {
        'events': Event.objects.filter(date_filter).order_by('start_date')
    })
