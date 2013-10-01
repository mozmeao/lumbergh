from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url('^position/(?P<job_id>[\w]+)$', views.position,
        name='careers.position'),
    url('^position/(?P<job_id>[\w]+)$', views.position,
        name='django_jobvite_position'),
    url('^/?$', views.home, name='careers.home'),
)
