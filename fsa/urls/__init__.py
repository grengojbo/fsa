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

import logging
log = logging.getLogger('fsa.urls') 

urlpatterns = basepatterns + shoppatterns + defaultpatterns
urlhelper.remove_duplicate_urls(urlpatterns, [])