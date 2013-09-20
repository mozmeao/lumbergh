from django.conf.urls.defaults import patterns, url

from careers.university import views


urlpatterns = patterns('',
    url('^university/$', views.index, name='university.index'),
)
