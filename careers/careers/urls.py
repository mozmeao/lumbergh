from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^position/wa/(?P<shortcode>[\w]+)$', views.WorkablePositionDetailView.as_view(),
        name='careers.workable_position'),
    url(r'^position/(?P<job_id>[\w]+)$', views.JobvitePositionDetailView.as_view(),
        name='careers.position'),
    url(r'^position/(?P<job_id>[\w]+)$', views.JobvitePositionDetailView.as_view(),
        name='django_jobvite_position'),
    url(r'^$', views.home, name='careers.home'),
    url(r'^listings/$', views.listings, name='careers.listings'),
]
