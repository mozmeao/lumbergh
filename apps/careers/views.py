from django.shortcuts import render, get_object_or_404

from django_jobvite.models import Position, Category


def home(request):
    excluded_categories = ['Internships', 'Volunteer and Community Opportunities']
    categories = list(Category.objects.exclude(
            name__in=excluded_categories).order_by('name'))
    internships = Category.objects.filter(name='Internships')
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
