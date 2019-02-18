from django.conf import settings
from django.conf.urls import include, url, re_path
from django.views.static import serve as servestatic

from .base import views

urlpatterns = [
    url(r'', include('careers.university.urls')),
    url(r'', include('careers.careers.urls')),

    # contribute.json url
    url(r'^(?P<path>contribute\.json)$', servestatic,
        kwargs={'document_root': settings.ROOT}),

    re_path(r'^.well-known/acme-challenge/(?P<path>.*)$',
            servestatic,
            {'document_root': settings.ROOT + '/.well-known/acme-challenge/'}),

    # Generate a robots.txt
    url(r'^robots\.txt$', views.robots, name='robots'),
    url(r'^404\.html$', views.custom_404, name='404'),
]

handler404 = 'careers.base.views.custom_404'
