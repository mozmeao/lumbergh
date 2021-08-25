from django.shortcuts import render
from bakery.views import BuildableTemplateView

# Create your views here.
class PositionsIndexPageTemplateView(BuildableTemplateView):
    build_path = 'positions/index.html'
    template_name = '/app/careers/positions/templates/positions/positions_index_page.html'