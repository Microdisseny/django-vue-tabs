from . import settings


class TabsMixin(object):
    class Media:
        css = {
            'all': ('django_vue_tabs/vue-tabs-component-1.1.0.css',)
        }
        js = []
        if settings.DJANGO_VUE_TABS_USE_VUE_JS:
            js.append('django_vue_tabs/vue-2.4.2.min.js')
        js += ['django_vue_tabs/vue-tabs-component-1.1.0.js',
               'django_vue_tabs/tabs.js']

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['tabs'] = self.tabs or []
        return super(TabsMixin, self).add_view(
            request, form_url=form_url,
            extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['tabs'] = self.tabs or []
        return super(TabsMixin, self).change_view(
            request, object_id=object_id, form_url=form_url,
            extra_context=extra_context)
