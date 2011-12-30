from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url('^$', views.home, name='careers.home'),
    url('^position/(?P<job_id>[\w]+)$', views.position, name='careers.position'),
)
