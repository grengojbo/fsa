# -*- mode: python; coding: utf-8; -*- 
from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from fsa.cdr.api.handlers import CdrHandler

auth = HttpBasicAuthentication(realm='FreeSWITCH Admin  API')

cdr = Resource(handler=CdrHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^$', cdr, name='cdr'),
    url(r'^phone/(?P<phone>.+)/query/(?P<start_date>.+)/(?P<end_date>.+)/$', cdr),
    url(r'^account/(?P<account>.+)/query/(?P<start_date>.+)/(?P<end_date>.+)/$', cdr),
    url(r'^phone/(?P<phone>.+)/$', cdr),
    url(r'^account/(?P<account>.+)/$', cdr),
)