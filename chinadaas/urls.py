from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.http import HttpResponseRedirect as redirect

from hbase.views import *
from company.views import *
from meta.views import *
from views import *
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chinadaas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
 	#url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.BASE_DIR + settings.STATIC_URL}),
	#url(r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
    url(r'^$', lambda x: redirect('/index/')),
    url(r'^index/$', index),
    url(r'^tologin/$', tologin),
    url(r'^login/$', login),
    url(r'^tochangepwd/$', to_change_pwd),
    url(r'^changepwd/$', change_pwd),
    url(r'^logout/$', logout),

    url(r'^hbase/tables/$', hbase_tables),
    url(r'^hbase/query/$', hbase_query),

    url(r'^guo/query/$', guo_query),

    url(r'^company/personlist/$', personlist),
    url(r'^company/linklist/$', linklist),
    url(r'^company/sharelist/$', sharelist),
    url(r'^company/macaddrlist/$', macaddrlist),
    url(r'^company/booklist/$', booklist),
    #url(r'^company/send_macaddr_mail/$', send_macaddr_mail),
    #url(r'^company/macaddredit/$', macaddredit),
    #url(r'^company/macaddrsubmit/$', macaddrsubmit),
    
	url(r'^meta/tablelist/$', tablelist),
	url(r'^meta/fieldlist/(\d+)/$', fieldlist),
)

from django.conf import settings
if settings.DEBUG is False:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.BASE_DIR + settings.STATIC_URL}),
	)
