# -*- mode: python; coding: utf-8; -*-
from django.conf.urls.defaults import *
from fsa.gateway import views

__author__ = '$Author: $'
__revision__ = '$Revision: $'

# place app url patterns here

urlpatterns = patterns(
    '',
    #url(r'^get/$', views.get),
    url(r'^gw/$', views.gw),
    )
