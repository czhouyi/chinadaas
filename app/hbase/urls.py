from django.conf.urls import patterns, url

from app.hbase.views import *

urlpatterns = patterns('',
    url(r'^table/$', table,    name='table'),
    url(r'^query/$',  query,    name='query'),
)