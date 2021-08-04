from django.conf.urls import url
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views
from .feeds import LatestPositionsFeed

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    url(r'^position/(?P<source>[\w]+)/(?P<job_id>[\w]+)/$', views.PositionDetailView.as_view(),
        name='careers.position'),
    url(r'^$', views.HomeView.as_view(), name='careers.home'),
    url(r'^feed/$', LatestPositionsFeed(), name='careers.feed'),
    url(r'^listings/$', views.PositionListView.as_view(), name='careers.listings'),
    url(r'^internships/$', views.InternshipsView.as_view(), name='careers.internships'),
    url(r'^benefits/$', views.BenefitsView.as_view(), name='careers.benefits'),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
