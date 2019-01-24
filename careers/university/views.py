from django.views.generic import TemplateView

from careers.careers.models import Position


class IndexView(TemplateView):
    template_name = 'university/index.jinja'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        open_for_applications = True

        param = context['view'].request.GET.get('open_for_applications')
        if param:
            open_for_applications = param == 'true'
        else:
            open_for_applications = Position.objects.filter(position_type='Intern').exists()

        context.update({
            'open_for_applications': open_for_applications,
        })

        return context
