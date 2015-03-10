from django.conf.urls import patterns, url

from app.company.views import *

urlpatterns = patterns('',
    url(r'^contact/$',  contact,    name='contact'),
    url(r'^link/$',     link,       name='link'),
    url(r'^share/$',    share,      name='share'),
    url(r'^book/$',     book,       name='book'),
)