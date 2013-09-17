from django.http import Http404
from django.shortcuts import render

from django_jobvite.models import Category, Position


def home(request):
    return render(request, 'careers/home.html', {
        'positions': Position.objects.order_by('category__name', 'title'),
        'categories': Category.objects.all(),
    })


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
