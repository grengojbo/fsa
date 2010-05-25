# -*- mode: python; coding: utf-8; -*-
from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from fsa.numberplan.api.handlers import NumberPlanHandler

auth = HttpBasicAuthentication(realm='FreeSWITCH Admin  API')

numberplan = Resource(handler=NumberPlanHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^$', numberplan, name='numberplan'),
    url(r'^(?P<phone>.+)/$', numberplan),
)
