# -*- mode: python; coding: utf-8; -*-
from django.conf.urls.defaults import *
#from fsa.gateway import views
from fsa.directory import views

__author__ = '$Author: $'
__revision__ = '$Revision: $'

# place app url patterns here
urlpatterns = patterns(
    '',
    #url(r'^get/$', v.gw),
    url(r'^(?P<object_id>\d+)/$', views.edit, name="directory_edit"),
    #url(r'^lists/$', views.directory_view, name="directory_view"),
    #url(r'^new/$', views.new_endpoint, name="new_endpoint"),
    )
