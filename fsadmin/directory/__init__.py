# -*- mode: python; coding: utf-8; -*-
from userprofile import signals
import logging
from fsadmin.directory.models import Endpoint
#from fsadmin.directory import signals as s

l = logging.getLogger('fsadmin.directory')

def handler_create_endpoint(sender, user, **kwargs):
    l.debug("Signal ProfileRegistration")
    new_endpoint = Endpoint.objects.create_endpoint(user)
    #s.endpoint_signal.send(user=user, endpoint=new_endpoint)
    
signals.profile_registration.connect(handler_create_endpoint)

