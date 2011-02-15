from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^defaults/', include('defaults.urls')),
    (r'^admin/catalog/', include('catalog.admin.urls')),
    (r'^admin/(.*)', admin.site.root),
    url(r'^', include('catalog.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )