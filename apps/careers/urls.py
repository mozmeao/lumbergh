from django.conf.urls.defaults import patterns, url

from careers import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='careers.home'),
    url(r'^position/(?P<job_id>[\w]+)$', views.position, name='careers.position'),
    url(r'^why?$', views.why, name='careers.why'),
)
