from django.shortcuts import render, get_object_or_404

from django_jobvite.models import Position, Category


def home(request):
    categories = Category.objects.exclude(name='Internships').order_by('name')
    internships = get_object_or_404(Category, name='Internships')
    return render(request, 'careers/home.html', {
        'categories': categories,
        'internships': internships,
    })


def position(request, job_id=None):
    position = Position.objects.select_related('category').get(job_id=job_id)
    positions = position.category.position_set.all()
    return render(request, 'careers/position.html', {
        'position': position,
        'positions': positions,
    }) 


def benefits(request):
    return render(request, 'careers/benefits.html')
