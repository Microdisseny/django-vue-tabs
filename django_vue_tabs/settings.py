from django.conf import settings

DJANGO_VUE_TABS_USE_VUE_JS = getattr(
    settings, 'DJANGO_VUE_TABS_USE_VUE_JS', True)
