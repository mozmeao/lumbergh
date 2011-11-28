from django.conf.urls.defaults import patterns


urlpatterns = patterns('',
    (r'^/?$', 'careers.views.careers'),
    (r'^benefits/?$', 'careers.views.benefits'),
    (r'^/(?P<slug>[\w-]+)/$', 'careers.views.department'),
    (r'^position/(?P<job_id>[\w]+)/$', 'careers.views.position'),
)
