# -*- coding:utf-8 -*-
from django import forms
from .models import TextManager
from loosecms.forms import PluginForm


class TextManagerForm(PluginForm):

    class Meta(PluginForm.Meta):
        model = TextManager