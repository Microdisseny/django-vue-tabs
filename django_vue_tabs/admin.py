from django import forms
from . import settings


class TabsMixin(object):
    change_form_template = 'django_vue_tabs/change_form.html'

    DJANGO_VUE_TABS_CSS = ['django_vue_tabs/vue-tabs-component-1.5.3.css']
    DJANGO_VUE_TABS_JS = (
        'django_vue_tabs/vue-tabs-component-1.5.3.js',
        'django_vue_tabs/tabs.js'
        )

    @property
    def media(self):
        css = super(TabsMixin, self).media._css
        if 'all' not in css:
            css['all'] = []
        css['all'].extend(self.DJANGO_VUE_TABS_CSS)
        js = super(TabsMixin, self).media._js
        if settings.DJANGO_VUE_TABS_USE_VUE_JS:
            js.append('django_vue_tabs/vue-2.6.11.min.js')
        js += self.DJANGO_VUE_TABS_JS
        return forms.Media(css=css, js=js)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if hasattr(self, 'tabs'):
            extra_context['tabs'] = self.tabs
        else:
            extra_context['tabs'] = []
        return super(TabsMixin, self).add_view(
            request, form_url=form_url,
            extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if hasattr(self, 'tabs'):
            extra_context['tabs'] = self.tabs
        else:
            extra_context['tabs'] = []
        return super(TabsMixin, self).change_view(
            request, object_id=object_id, form_url=form_url,
            extra_context=extra_context)
