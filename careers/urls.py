from django.conf import settings
from django.conf.urls import include, url
from django.views.static import serve as servestatic

from .base import views

urlpatterns = [
    url(r'', include('careers.university.urls')),
    url(r'', include('careers.careers.urls')),

    # contribute.json url
    url(r'^(?P<path>contribute\.json)$', servestatic,
        kwargs={'document_root': settings.ROOT}),

    # Generate a robots.txt
    url(r'^robots\.txt$', views.robots, name='robots'),
]
