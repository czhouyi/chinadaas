from django.conf.urls import patterns, url

from app.meta.views import *

urlpatterns = patterns('',
	url(r'^table/$',		table,	name='table'),
	url(r'^field/(\d+)/$',	field,	name='field'),
)