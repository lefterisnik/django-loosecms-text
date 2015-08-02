# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import TextManager
from .plugin import TextPlugin

admin.site.register(TextManager, TextPlugin)