# -*- mode: python; coding: utf-8; -*- 
from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from fsa.lcr.api.handlers import LcrHandler
##
auth = HttpBasicAuthentication(realm='FreeSWITCH Admin  API')

lcr = Resource(handler=LcrHandler, authentication=auth)
##
urlpatterns = patterns('',
    url(r'^$', lcr),
    url(r'^doc/$', documentation_view),
    #url(r'^(?P<start>.+)/(?P<limit>.+)/$', endpoint),
    url(r'^(?P<phone>.+)/$', lcr),
    #url(r'^posts\.(?P<emitter_format>.+)', blogposts, name='blogposts'),

    # automated documentation
)