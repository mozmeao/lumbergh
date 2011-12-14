from django.conf.urls.defaults import patterns, url

from careers import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='careers.home'),
    url(r'^benefits?$', views.benefits, name='careers.benefits'),
    url(r'^position/(?P<job_id>[\w]+)$', views.position, name='careers.position'),
)
