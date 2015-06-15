from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^position/wa/(?P<shortcode>[\w]+)$', views.WorkablePositionDetailView.as_view(),
        name='careers.workable_position'),
    url(r'^position/(?P<job_id>[\w]+)$', views.position,
        name='careers.position'),
    url(r'^position/(?P<job_id>[\w]+)$', views.position,
        name='django_jobvite_position'),
    url(r'^$', views.home, name='careers.home'),
    url(r'^listings/$', views.listings, name='careers.listings'),
)
