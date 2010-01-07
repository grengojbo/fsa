# -*- mode: python; coding: utf-8; -*-
"""
views.py

Created by jbo on 2009-12-13.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""
from django.conf import settings
from django.http import HttpResponseNotFound
#from sugar.views.decorators import render_to
#from lib.http import HttpResponseRedirectView
from fsa.core import is_app

import logging

l = logging.getLogger('fsa.api.views')

__author__ = '$Author:$'
__revision__ = '$Revision:$'

def get(request):
    try:
        l.debug("post: %s" % request.POST)
        if request.POST['section'] == "configuration":
            try:
                # TODO добавить загрузку конфигурации lcr.conf
                from fsa.server import views as sv
                if (request.POST.get('key_value') == "event_socket.conf"):
                    l.debug("key_ value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
                    return sv.get_event_socket(request)
                elif (request.POST['key_value'] == "acl.conf"):
                    from fsa.acl import views as av
                    l.debug("key_ value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
                    return av.get(request)
                elif (request.POST['key_value'] == "limit.conf"):
                    l.debug("key_ value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
                    return sv.get_limit(request)
                elif (request.POST['key_value'] == "post_load_modules.conf"):
                    l.debug("key_ value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
                    return sv.post_modules(request)
                elif (request.POST['key_value'] == "post_load_switch.conf"):
                    l.debug("key_ value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
                    return sv.post_switch(request) 
                elif (request.POST['key_value'] == "sofia.conf"):
                    l.debug("key_ value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
                    return sv.get_sofia(request)
                else:
                    return sv.get(request)
            except Exception, e:
                l.error("Error import module: %s" % e)
    except Exception, e:
        l.error("Error generating confg %s" % e)
        return HttpResponseNotFound('<h1>Error generating config</h1>')