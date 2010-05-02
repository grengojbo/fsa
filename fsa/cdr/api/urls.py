# -*- mode: python; coding: utf-8; -*- 
from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from fsa.cdr.api.handlers import CdrHandler
##
auth = HttpBasicAuthentication(realm='FreeSWITCH Admin  API')

cdr = Resource(handler=CdrHandler, authentication=auth)
##
urlpatterns = patterns('',
    url(r'^$', cdr),
    url(r'^doc/$', documentation_view),
    #url(r'^(?P<start>.+)/(?P<limit>.+)/$', endpoint),
    url(r'^(?P<phone>.+)/$', cdr),
    #url(r'^posts\.(?P<emitter_format>.+)', blogposts, name='blogposts'),

    # automated documentation
)