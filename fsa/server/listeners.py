# -*- mode: python; coding: utf-8; -*-
"""
listeners.py

Created by jbo on 2010-01-08.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
from signals_ahoy import signals
from signals_ahoy.asynchronous import AsynchronousListener
from django.contrib.auth.models import User
#from fsa.directory.signals import endpoint_create
import keyedcache
from django.db import models
#from fsa.directory.signals import *
from django.db.models.signals import pre_save
from fsa.server.models import SipProfile
#from urls import custompatterns
#import localsite
import logging
import time

log = logging.getLogger('fsa.server.listeners')

def clean_cache_siprofile_handler(sender, **kwargs):
    ipn_obj = kwargs['instance']
    key_caches = "directory::gw::sites::{0}".format(ipn_obj.name)
    keyedcache.cache_delete(key_caches)

def start_listening():
    #models.signals.post_save.connect(handler_create_endpoint, sender=User)
    log.debug('Added server listeners')
    pre_save.connect(clean_cache_siprofile_handler, sender=SipProfile)
