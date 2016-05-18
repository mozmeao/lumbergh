from django.conf.urls import url

from . import views
from .feeds import LatestPositionsFeed

urlpatterns = [
    url(r'^position/(?P<job_id>[\w]+)$', views.JobvitePositionDetailView.as_view(),
        name='careers.position'),
    url(r'^position/(?P<job_id>[\w]+)$', views.JobvitePositionDetailView.as_view(),
        name='django_jobvite_position'),
    url(r'^$', views.home, name='careers.home'),
    url(r'^feed/$', LatestPositionsFeed(), name='careers.feed'),
    url(r'^listings/$', views.listings, name='careers.listings'),
]
