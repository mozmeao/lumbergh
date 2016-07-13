from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import get_object_or_404

from careers.careers.forms import PositionFilterForm
from careers.careers.models import Position


class HomeView(TemplateView):
    template_name = 'careers/home.jinja'


class PositionListView(ListView):
    model = Position
    template_name = 'careers/listings.jinja'
    context_object_name = 'positions'

    def get_context_data(self, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)
        context['form'] = PositionFilterForm(self.request.GET or None)
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
        related_positions = (
            Position.objects.filter(department=position.department).exclude(id=position.id))
        context['related_positions'] = related_positions
        return context
