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
import config
from django.db import models
#from fsa.directory.signals import *

#from fsa.directory.models import Endpoint
#from urls import custompatterns
#import localsite
import logging
import time

log = logging.getLogger('fsa.server.listeners')

# def add_custom_urls(sender, patterns=(), **kwargs):
#     log.debug('adding custom urls')
#     patterns += custompatterns
#     
# def delay_and_note(sender, note="", **kwargs):
#     log.debug('delaying before adding a note')
#     time.sleep(5)
#     from models import Note
#     Note.objects.create(note=note)
#     log.debug('added a note')
#     
# delayedNote = AsynchronousListener(delay_and_note)
# 
# def start_listening():
#     signals.collect_urls.connect(add_custom_urls, sender=localsite)
#     async_note.connect(delayedNote.listen, sender=None)

##def handler_create_endpoint(sender, **kwargs):
##    log.debug("Signal post save User")
##    if sender.is_active() and config_value('directory', 'AUTO_CREATE'):
##        new_endpoint = Endpoint.objects.create_endpoint(sender)
##        endpoint_create.send(sender=Endpoint, endpoint=new_endpoint)
##        log.debug('Send signal endpoint_create')
##    else:
##        log.debug('User no active or config value AUTO_CREATE=False')
##     
# signals.profile_registration.connect(handler_create_endpoint)

def start_listening():
    #models.signals.post_save.connect(handler_create_endpoint, sender=User)
    log.debug('Added server listeners')
    
