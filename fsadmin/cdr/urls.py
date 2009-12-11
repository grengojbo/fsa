# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
#from django.utils.translation import ugettext_lazy as _
from fsadmin.cdr import views

__author__ = '$Author: $'
__revision__ = '$Revision: $'

# place app url patterns here
urlpatterns = patterns(
    '',
    url(r'^get/$', views.get),
    url(r'^set/$', views.set),
    url(r'^xml/$', views.get_xml_conf),
    url(r'^csv/$', views.get_csv_conf),
    )
