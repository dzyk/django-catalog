# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from catalog import settings as catalog_settings

urlpatterns = patterns('')

if catalog_settings.CATALOG_URL_SHEME == 'id':
    urlpatterns += patterns('catalog.views',
        url(r'^(?P<slug>.*)-(?P<item_id>\d{1,7})/$', 'tree', name='tree'),
    )
elif catalog_settings.CATALOG_URL_SHEME == 'slug':
    urlpatterns += patterns('catalog.views',
        url(r'^(?P<slug>.*)-(?P<item_id>\d{1,7})/$', 'tree', name='tree'),
    )

if catalog_settings.CATALOG_ROOT_PAGE:
    urlpatterns += patterns('catalog.views',
        url(r'^$', 'tree', name='catalog_root_page'),
    )
