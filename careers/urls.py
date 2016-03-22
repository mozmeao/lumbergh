from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from base import views

urlpatterns = [
    url(r'', include('careers.university.urls')),
    url(r'', include('careers.careers.urls')),

    # contribute.json url
    url(r'^(?P<path>contribute\.json)$', 'django.views.static.serve',
        {'document_root': settings.ROOT}),

    # Generate a robots.txt
    url(r'^robots\.txt$', views.robots, name='robots'),
]


if settings.SAML_ENABLE:
    urlpatterns += [
        url(r'^saml2/', include('careers.saml.urls'))
    ]


if settings.ENABLE_ADMIN:
    urlpatterns += [
        url(r'^admin/', include(admin.site.urls)),
    ]
    admin.site.site_header = 'Careers Administration'
    admin.site.site_title = 'Mozilla Careers'
