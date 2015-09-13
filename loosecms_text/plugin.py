# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from .models import *

from loosecms.plugin_pool import plugin_pool
from loosecms.plugin_modeladmin import PluginModelAdmin


class TextPlugin(PluginModelAdmin):
    model = Text
    name = _('Text')
    template = "plugin/text.html"
    plugin = True

    def update_context(self, context, manager):
        context['text'] = manager
        return context

plugin_pool.register_plugin(TextPlugin)