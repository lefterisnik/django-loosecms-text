# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from loosecms.models import Plugin
from ckeditor.fields import RichTextField

import os


class TextManager(Plugin):
    title = models.CharField(_('title'), max_length=200,
                             help_text='Give some title.')
    body = RichTextField(_('body'))

    ctime = models.DateTimeField(editable=False, auto_now_add=True)

    utime = models.DateTimeField(auto_now=True)

    published = models.BooleanField(_('published'), default=True)

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)