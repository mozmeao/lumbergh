
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import get_object_or_404

from careers.careers.forms import PositionFilterForm
from careers.careers.models import Position
from careers.careers.utils import generate_position_meta_description
from careers.careers.wordpress import get_posts


class HomeView(TemplateView):
    template_name = 'careers/home.jinja'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        featured_post, recent_posts = get_posts()

        context['featured_post'] = featured_post
        context['recent_posts'] = recent_posts
        return context


class InternshipsView(TemplateView):
    template_name = 'careers/internships.jinja'


class BenefitsView(TemplateView):
    template_name = 'careers/benefits.jinja'
    

class PositionListView(ListView):
    model = Position
    template_name = 'careers/listings.jinja'
    context_object_name = 'positions'

    def get_context_data(self, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)
        context['form'] = PositionFilterForm()
        return context


class PositionDetailView(DetailView):
    model = Position
    context_object_name = 'position'
    template_name = 'careers/position.jinja'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, **self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(PositionDetailView, self).get_context_data(**kwargs)
        position = context['position']

        context['meta_description'] = generate_position_meta_description(position)

        related_positions = (
            Position.objects.filter(department=position.department).exclude(id=position.id))
        context['related_positions'] = related_positions

        return context
