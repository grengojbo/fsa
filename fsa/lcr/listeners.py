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
from livesettings import config_value, config_value_safe
from django.db import models
from django.db.models.signals import pre_save
#from fsa.directory.signals import *
import keyedcache
from fsa.lcr.models import Lcr
import logging
import time

log = logging.getLogger('fsa.gateway.listeners')

def clean_cache_lcr_handler(sender, **kwargs):
    ipn_obj = kwargs['instance']
    #key_caches_phone_site = "phone::{0}::site::{1}".format(ipn_obj.digits, ipn_obj.site)
    #keyedcache.cache_delete(key_caches_phone_site)

def start_listening():
    log.debug('Added Lcr listeners')
    #pre_save.connect(clean_cache_lcr_handler, sender=Lcr)
