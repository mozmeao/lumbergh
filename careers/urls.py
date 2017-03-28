from django.conf import settings
from django.conf.urls import include, url

from base import views

urlpatterns = [
    url(r'', include('careers.university.urls')),
    url(r'', include('careers.careers.urls')),

    # contribute.json url
    url(r'^(?P<path>contribute\.json)$', 'django.views.static.serve',
        {'document_root': settings.ROOT}),

    # Generate a robots.txt
    url(r'^robots\.txt$', views.robots, name='robots'),
    # Generate a robots.txt
    url(r'^csp-violation-capture$', views.csp_violation_capture,
        name='csp-violation-capture'),
]
