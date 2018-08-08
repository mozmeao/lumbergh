from django.conf.urls import url

from careers.university import views


urlpatterns = [
    url('^university/$', views.IndexView.as_view(), name='university.index'),
]
