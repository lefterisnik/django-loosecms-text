# -*- coding: utf-8 -*-
from django.conf.urls import url, include

app_urlpatterns = [
    url(r'^ckeditor/', include('ckeditor.urls')),
]

urlpatterns = []