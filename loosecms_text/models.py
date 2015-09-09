# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from loosecms.models import Plugin
from loosecms.fields import LoosecmsRichTextField


class Text(Plugin):
    default_type = 'TextPlugin'

    title = models.CharField(_('title'), max_length=200,
                             help_text='Give some title.')
    body = LoosecmsRichTextField(_('body'))

    ctime = models.DateTimeField(auto_now_add=True)

    utime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)