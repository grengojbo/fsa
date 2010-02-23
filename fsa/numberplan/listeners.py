# -*- mode: python; coding: utf-8; -*- 
from signals_ahoy import signals
#from django import forms
from fsa.numberplan.models import NumberPlan
from fsa.directory.signals import endpoint_change, endpoint_create, endpoint_delete
import logging
log = logging.getLogger('fsb.numberplan.listeners')

def create_phone_number(sender, endpoint, **kwargs):
    log.debug(sender)
    try:
        NumberPlan.objects.lactivate(endpoint.uid)
        log.debug('activate phone number: %s' % endpoint.uid)
    except NumberPlan.DoesNotExist:
        new_phoen = NumberPlan.objects.create_phone_number(endpoint.uid)
        log.debug('activate phone number: %s' % new_phoen.phone_number)
    
def change_phone_number(sender, endpoint, old_endpoint, **kwarg):
    NumberPlan.objects.lpark(old_endpoint.uid)
    NumberPlan.objects.lactivate(endpoint.uid)

def park_phone_number(endpoint, **kwargs):
    NumberPlan.objects.lpark(endpoint)
    
def start_listening():
    endpoint_create.connect(create_phone_number)
    endpoint_change.connect(change_phone_number)
    endpoint_delete.connect(park_phone_number, sender=None)
    log.debug('Added number plan listeners')