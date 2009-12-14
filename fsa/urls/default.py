# -*- mode: python; coding: utf-8; -*-
"""
default.py

Created by jbo on 2009-08-24.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

from django.conf import settings
from django.conf.urls.defaults import *

import logging
log = logging.getLogger('fsa.urls.default')
log.debug("Adding local serving of admin files at: %s", settings.ADMIN_MEDIA_ROOT)
urlpatterns = patterns('',
    (r'^admin-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes': True}),
)

#The following is used to serve up local media files like images
if getattr(settings, 'LOCAL_DEV', False):
    log.debug("Adding local serving of static files at: %s", settings.MEDIA_ROOT)
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,'show_indexes': True}),
        (r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,'show_indexes': True}), 
        
    )

