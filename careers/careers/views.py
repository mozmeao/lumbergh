from django.conf import settings
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import get_object_or_404
from jinja2 import Markup

import requests

from careers.careers.forms import PositionFilterForm
from careers.careers.models import Position
from careers.careers.wordpress import complete_posts_data, get_posts_data, process_excerpt


class HomeView(TemplateView):
    template_name = 'careers/home.jinja'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        # blog content isn't critical to the page. if the wordpress API fails
        # for some reason, we can just move on and wait for the next build
        try:
            posts_data = get_posts_data()
            blog_posts = []

            if posts_data:
                complete_posts_data(posts_data)

                for post in posts_data:
                    blog_posts.append({
                        'title': Markup(post['title']['rendered']).unescape(),
                        'link': post['link'],
                        'excerpt': Markup(process_excerpt(post['excerpt']['rendered'])),
                        'image': post['featured_media']['media_details']['sizes']['post-large']['source_url'],  # noqa
                    })

                # notify dms when blog posts are successfully fetched
                if (settings.DMS_BLOG_FETCH):
                    requests.get(settings.DMS_BLOG_FETCH)
        except Exception:
            blog_posts = []

        context['blog_posts'] = blog_posts
        return context


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
        related_positions = (
            Position.objects.filter(department=position.department).exclude(id=position.id))
        context['related_positions'] = related_positions
        return context
