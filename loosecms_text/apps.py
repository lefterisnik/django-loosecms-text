# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LooseCMSTextConfig(AppConfig):
    name = 'loosecms_text'
    verbose_name = _('Loose CMS Plugin - Text')
