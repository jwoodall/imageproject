# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('imageproject.myapp.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^show/$', 'show', name='show'),
)
