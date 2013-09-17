from django.http import Http404
from django.shortcuts import render

from django_jobvite.models import Position, Category


def home(request):
    excluded_categories = ['Volunteer and Community Opportunities']
    categories = Category.objects.exclude(name__in=excluded_categories).order_by('name')

    return render(request, 'careers/home.html', {
        'categories': categories,
    })

def university(request):
    return render(request, 'careers/university.html', { })


def position(request, job_id=None):
    try:
        position = Position.objects.select_related('category').get(job_id__contains=job_id)
        positions = position.category.position_set.all()

        # Add applicant source param for jobvite
        position.apply_url += '&s=PDN'

        return render(request, 'careers/position.html', {
            'position': position,
            'positions': positions,
        })
    except Position.DoesNotExist:
        raise Http404
