from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from django_jobvite import models as jobvite_models

import utils
from careers.careers.forms import PositionFilterForm
from careers.django_workable import models as workable_models


def home(request):
    return render(request, 'careers/home.html')


def listings(request):
    return render(request, 'careers/listings.html', {
        'positions': utils.get_all_positions(
            order_by=lambda x: u'{0} {1}'.format(x.category.name, x.title)),
        'form': PositionFilterForm(request.GET or None),
    })


def position(request, job_id=None):
    # Cannot use __exact instead of __contains due to MySQL collation
    # which does not allow case sensitive matching.
    position = get_object_or_404(jobvite_models.Position, job_id__contains=job_id)
    positions = utils.get_all_positions(filters={'category__name': position.category.name},
                                        order_by=lambda x: x.title)

    # Add applicant source param for jobvite
    position.apply_url += '&s=PDN'

    return render(request, 'careers/position.html', {
        'position': position,
        'positions': positions,
    })


class WorkablePositionDetailView(DetailView):
    context_object_name = 'position'
    model = workable_models.Position
    template_name = 'careers/position.html'
    slug_field = 'shortcode'
    slug_url_kwarg = 'shortcode'

    def get_context_data(self, **kwargs):
        context = super(WorkablePositionDetailView, self).get_context_data(**kwargs)
        context['positions'] = utils.get_all_positions(
            filters={'category__name': context['position'].category.name},
            order_by=lambda x: x.title)
        return context
