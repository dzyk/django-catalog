from django.conf import settings
import os.path

# URL that handles catalog's media and uses <MEDIA_ROOT>/catalog by default.
CATALOG_MEDIA_URL = getattr(settings, 'CATALOG_MEDIA_URL', os.path.join(settings.MEDIA_URL, 'catalog/'))

DEFAULT_CATALOG_CONNECTED_MODELS = [
    ('catalog.models.Item', 'catalog.admin.ItemAdmin'),
    ('catalog.models.Section', 'catalog.admin.SectionAdmin'),
    ('catalog.models.MetaItem', None),
]

CATALOG_CONNECTED_MODELS = getattr(settings, 'CATALOG_CONNECTED_MODELS', DEFAULT_CATALOG_CONNECTED_MODELS)
