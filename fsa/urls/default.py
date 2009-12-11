# -*- mode: python; coding: utf-8; -*-
"""
default.py

Created by jbo on 2009-08-24.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
import logging
log = logging.getLogger('fsa.urls.default')

admin.autodiscover()

urlpatterns = getattr(settings, 'URLS', [])

adminpatterns = patterns('',
     (r'^admin/', include(admin.site.urls)),
)

if urlpatterns:
    urlpatterns += adminpatterns
else:
    urlpatterns = adminpatterns

#The following is used to serve up local media files like images
if getattr(settings, 'LOCAL_DEV', False):
    log.debug("Adding local serving of static files at: %s", settings.MEDIA_ROOT)
    baseurlregex = r'^static/(?P<path>.*)$' 
    urlpatterns += patterns('',
        (baseurlregex, 'django.views.static.serve',
        {'document_root':  settings.MEDIA_ROOT}),
        
        (r'^site_media/(.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT}),        
    )

