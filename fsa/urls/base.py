# -*- mode: python; coding: utf-8; -*-
"""
base.py

Created by jbo on 2009-12-05.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""
from django.conf.urls.defaults import *
from signals_ahoy.signals import collect_urls
import logging
import fsa
from os.path import join, dirname
log = logging.getLogger('fsa.urls.base')

fsa_urlpatterns = patterns('',
    (r'^api/', include('fsa.api.urls')),
    #url(r'^xmlcurl/', include('fsadmin.xmlcurl.urls')),
    #url(r'^server/', include('fsa.server.urls')),
    #url(r'^dialplan/', include('fsa.dialplan.urls')),
    #url(r'^directory/', include('fsadmin.directory.urls')),
    #url(r'^cdr/', include('fsa.cdr.urls')),
    #url(r'^acl/', include('fsa.acl.urls')),
    url(r'^gw/', include('fsa.gateway.urls')),
) 

urlpatterns = patterns('',
    #(r'^accounts/', include('satchmo_store.accounts.urls')),
    #url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog', name="i18n-js"),
    (r'^settings/', include('livesettings.urls')),
    (r'^cache/', include('keyedcache.urls')),
) + fsa_urlpatterns

collect_urls.send(sender=fsa, patterns=urlpatterns)
