# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from .models import *
from .forms import *

from loosecms.plugin_pool import plugin_pool
from loosecms.plugin_modeladmin import PluginModelAdmin


class TextPlugin(PluginModelAdmin):
    model = TextManager
    name = _('Text')
    form = TextManagerForm
    template = "plugin/text.html"
    plugin = True
    extra_initial_help = None
    fields = ('type', 'placeholder', 'title', 'body', 'published')

    def update_context(self, context, manager):
        context['text'] = manager
        return context

    def get_changeform_initial_data(self, request):
        initial = {}
        if self.extra_initial_help:
            initial['type'] = self.extra_initial_help['type']
            initial['placeholder'] = self.extra_initial_help['placeholder']
            initial['manager'] = self.extra_initial_help['page']

            return initial
        else:
            return {'type': 'TextPlugin'}

plugin_pool.register_plugin(TextPlugin)