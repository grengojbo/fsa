# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from fsadmin.directory import views

__author__ = '$Author: $'
__revision__ = '$Revision: $'

# place app url patterns here
urlpatterns = patterns(
    '',
    url(r'^get/$', views.get),
    )
