from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^about/$', about, name='about'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('app.account.urls')),
    url(r'^hbase/', include('app.hbase.urls')),
    url(r'^company/', include('app.company.urls')),
    url(r'^meta/', include('app.meta.urls')),
)

from django.conf import settings
if settings.DEBUG is False:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.BASE_DIR + settings.STATIC_URL}),
	)
