from django.shortcuts import render
from django.views.generic import DetailView

from django_jobvite import models as jobvite_models

import utils
from careers.careers.forms import PositionFilterForm
from careers.django_workable import models as workable_models


def home(request):
    return render(request, 'careers/home.jinja')


def listings(request):
    return render(request, 'careers/listings.jinja', {
        'positions': utils.get_all_positions(
            order_by=lambda x: u'{0} {1}'.format(x.category.name, x.title)),
        'form': PositionFilterForm(request.GET or None),
    })


class JobvitePositionDetailView(DetailView):
    context_object_name = 'position'
    model = jobvite_models.Position
    template_name = 'careers/position.jinja'
    slug_field = 'job_id'
    slug_url_kwarg = 'job_id'

    def get_context_data(self, **kwargs):
        context = super(JobvitePositionDetailView, self).get_context_data(**kwargs)

        # Add applicant source param for jobvite
        context['position'].apply_url += '&s=PDN'

        context['positions'] = utils.get_all_positions(
            filters={'category__name': context['position'].category.name},
            order_by=lambda x: x.title)
        return context


class WorkablePositionDetailView(DetailView):
    context_object_name = 'position'
    model = workable_models.Position
    template_name = 'careers/position.jinja'
    slug_field = 'shortcode'
    slug_url_kwarg = 'shortcode'

    def get_context_data(self, **kwargs):
        context = super(WorkablePositionDetailView, self).get_context_data(**kwargs)
        context['positions'] = utils.get_all_positions(
            filters={'category__name': context['position'].category.name},
            order_by=lambda x: x.title)
        return context
