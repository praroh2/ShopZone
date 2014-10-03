from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('store.urls')),
    url(r'^shop/', include('store.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

