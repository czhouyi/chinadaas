from django.conf.urls import patterns, url

from app.account.views import *

urlpatterns = patterns('',
        url(r'^sign_in/$',       sign_in,          name='sign_in'),
        url(r'^do_sign_in/$',    do_sign_in,       name='do_sign_in'),
        url(r'^sign_up/$',       sign_up,          name='sign_up'),
        url(r'^do_sign_up/$',    do_sign_up,       name='do_sign_up'),
        url(r'^change_pwd/$',    change_pwd,       name='change_pwd'),
        url(r'^do_change_pwd/$', do_change_pwd,    name='do_change_pwd'),
        url(r'^sign_out/$',      sign_out,         name='sign_out'),
)