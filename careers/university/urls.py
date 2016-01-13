from django.conf.urls import url

from careers.university import views


urlpatterns = [
    url('^university/$', views.index, name='university.index'),
]
