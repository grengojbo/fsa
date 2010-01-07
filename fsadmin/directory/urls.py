# -*- mode: python; coding: utf-8; -*-
from django.conf.urls.defaults import *
from django.conf import settings
from fsadmin.directory import views

__author__ = '$Author: $'
__revision__ = '$Revision: $'

# place app url patterns here
urlpatterns = patterns(
    '',
    url(r'^get/$', views.get),
    url(r'^edit/(?P<object_id>\d+)/$', views.directory_edit, name="directory_edit"),
    url(r'^lists/$', views.directory_view, name="directory_view"),
    url(r'^new/$', views.new_endpoint, name="new_endpoint"),
    )
