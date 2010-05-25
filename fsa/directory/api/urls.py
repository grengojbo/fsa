# -*- mode: python; coding: utf-8; -*- 
from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from fsa.directory.api.handlers import EndpointHandler
##
auth = HttpBasicAuthentication(realm='FreeSWITCH Admin  API')

endpoint = Resource(handler=EndpointHandler, authentication=auth)
##
urlpatterns = patterns('',
    url(r'^$', endpoint, name='endpoint'),
    url(r'^account/(?P<account>.+)/$', endpoint),
    url(r'^phone/(?P<phone>.+)/$', endpoint),
)