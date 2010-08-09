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
from fsa.gateway.models import SofiaGateway
import logging
import time

log = logging.getLogger('fsa.gateway.listeners')

def clean_cache_gw_handler(sender, **kwargs):
    ipn_obj = kwargs['instance']
    key_caches_gw = "gatewayw::{0}".format(ipn_obj.name)
    keyedcache.cache_delete(key_caches_gw)

def start_listening():
    log.debug('Added Gateway listeners')
    pre_save.connect(clean_cache_gw_handler, sender=SofiaGateway)
