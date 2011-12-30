from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='careers.home'),
    url(r'^position/(?P<job_id>[\w]+)$', views.position, name='careers.position'),
)
