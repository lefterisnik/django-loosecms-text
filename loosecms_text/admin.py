# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Text
from .plugin import TextPlugin

admin.site.register(Text, TextPlugin)