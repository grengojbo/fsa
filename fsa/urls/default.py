# -*- mode: python; coding: utf-8; -*-
"""
default.py

Created by jbo on 2009-08-24.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""
from os.path import join, dirname
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import logging
log = logging.getLogger('fsa.urls.default')

#The following is used to serve up local media files like images
if getattr(settings, 'LOCAL_DEV', False):
    log.debug("Adding local serving of media files at: %s", settings.MEDIA_ROOT)
    try:
        import grappelli
        urlpatterns = patterns('',
            #('^admin-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': join(dirname(grappelli.__path__[0]), 'grappelli/media')}),
            #(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,'show_indexes': True}),
            (r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,'show_indexes': True}), 
        )
        #log.debug("Adding local serving of admin files at: %s",  join(dirname(grappelli.__path__[0]), 'grappelli/media'))
    except:
        from django.contrib import admin
        urlpatterns = patterns('',
            #('^admin-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': join(dirname(admin.__file__), 'media')}),
            #(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,'show_indexes': True}),
            (r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,'show_indexes': True}), 
        )
        #log.debug("Adding local serving of admin files at: %s", join(dirname(admin.__file__), 'media'))
    #log.debug("Adding local serving of admin files at: %s", settings.ADMIN_MEDIA_ROOT)
    #(r'^admin-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes': True}),
#else:
#    log.debug("Adding local serving of admin files at: %s", settings.ADMIN_MEDIA_ROOT)
#    urlpatterns = patterns('',
#        (r'^admin-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes': True}),
#    )

urlpatterns += staticfiles_urlpatterns()