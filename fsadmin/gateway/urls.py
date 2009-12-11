# -*- mode: python; coding: utf-8; -*-
from django.conf.urls.defaults import *
from fsadmin.gateway import views

__author__ = '$Author: $'
__revision__ = '$Revision: $'

# place app url patterns here

urlpatterns = patterns(
    '',
    url(r'^get/$', views.get),
    )
