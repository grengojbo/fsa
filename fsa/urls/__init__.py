# -*- mode: python; coding: utf-8; -*- 
"""
__init__.py

Created by jbo on 2009-08-24.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

from base import urlpatterns as basepatterns
from default import urlpatterns as defaultpatterns
from django.conf.urls.defaults import *
import urlhelper

handler404 = 'djanjinja.handlers.page_not_found'
handler500 = 'djanjinja.handlers.server_error'

import logging
log = logging.getLogger('fsa.urls') 

urlpatterns = basepatterns + defaultpatterns
urlhelper.remove_duplicate_urls(urlpatterns, [])