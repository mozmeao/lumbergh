from django.conf.urls import url
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views
from .feeds import LatestPositionsFeed

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from careers.home import views as homeViews

urlpatterns = [
    url(r'^v1/position/(?P<source>[\w]+)/(?P<job_id>[\w]+)/$', views.PositionDetailView.as_view(),
        name='careers.position'),
    url(r'^v1/$', views.HomeView.as_view(), name='careers.home'),
    url(r'^v1/feed/$', LatestPositionsFeed(), name='careers.feed'),
    url(r'^v1/listings/$', views.PositionListView.as_view(), name='careers.listings'),
        
    # For Docker Flow.
    url(r'^__heartbeat__/$', views.HeartBeatView.as_view(), name='careers.heartbeat'),
    url(r'^__lbheartbeat__/$', views.LBHeartBeatView.as_view(), name='careers.lbheartbeat'),
    url(r'^__version__/$', views.VersionView.as_view(), name='careers.version'),

    path('cms/', include(wagtailadmin_urls)),
    # path('documents/', include(wagtaildocs_urls)),
    path('', include(wagtail_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
