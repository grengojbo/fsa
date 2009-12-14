# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import *

# place app url patterns here
from fsa.server import views

urlpatterns = patterns(
    '',
    url(r'^get/$', views.get),
    url(r'^event/$', views.get_event_socket),
    url(r'^sofia/$', views.get_sofia),
    #url(r'^logout/$', views.logout, name="logout"),
    #url(r'^auth/$', views.auth, name="auth"),
    )
