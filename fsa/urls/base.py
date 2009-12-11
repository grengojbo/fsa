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

log = logging.getLogger('fsa.urls.base')

fsa_urlpatterns = patterns('',
    url(r'^xmlcurl/', include('fsadmin.xmlcurl.urls')),
    url(r'^server/', include('fsadmin.server.urls')),
    url(r'^dialplan/', include('fsadmin.dialplan.urls')),
    url(r'^directory/', include('fsadmin.directory.urls')),
    url(r'^cdr/', include('fsadmin.cdr.urls')),
) 

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^accounts/', include('satchmo_store.accounts.urls')),
    (r'^settings/', include('livesettings.urls')),
    (r'^cache/', include('keyedcache.urls')),
) + fsa_urlpatterns

collect_urls.send(sender=fsa, patterns=urlpatterns)

