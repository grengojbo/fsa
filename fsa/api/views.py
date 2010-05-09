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

def directory(request):
    """directory"""
    try:
        l.debug("post: %s" % request.POST)
        if request.POST['section'] == "directory":
            from fsa.directory import views as d
            from fsa.gateway import views as gw
            from fsa.server import views as sv
            if request.POST.get('profile') and request.POST['purpose'] == 'gateways':
                # TODO сейчас выдает пустушку но если раскоментировать то будет выдавать список шлюзов
                # но тогда наверное нужно убрать из server/sip_profile.xml секцию gateways  
                # но зачем это надо непойму и так они подгружаются через server/sip_profile
                #return gw.profile(request)
                return d.gateways(request)
            elif request.POST.get('purpose') == 'network-list':
                # TODO так и непонял нах оно надо в доке пишут
                # This last post is regarding mod_sofia asking for users with cidr = attributes for adding them to the acls.
                return sv.get(request)
            else:
                return d.set(request)
            #elif request.POST.get('sip_auth_nc'):
            #    return d.set(request)
            #else:
            #    return sv.get(request)
        else:
            l.debug("IS NOT section %s " % request.POST.get('section'))
            return HttpResponseNotFound('<h1>section %s</h1>' % request.POST.get('section'))
    except Exception, e:
        l.error("Error generating confg %s" % e)
        return HttpResponseNotFound('<h1>Error generating config</h1>')
    
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
                elif (request.POST['key_value'] == "odbc_query.conf"):
                    l.debug("key_ value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
                    return sv.odbc_query(request)
                elif (request.POST['key_value'] == "post_load_switch.conf"):
                    l.debug("key_ value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
                    return sv.post_switch(request) 
                elif (request.POST['key_value'] == "sofia.conf"):
                    l.debug("key_ value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
                    return sv.get_sofia(request)
                elif (request.POST['key_value'] == "nibblebill.conf"):
                    l.debug("key_ value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
                    from fsb.billing import views as bill
                    return bill.get_conf(request)
                elif (request.POST['key_value'] == "xml_cdr.conf"):
                    from fsa.cdr import views as cv
                    l.debug("key_ value xml_cdr.conf hostname: %s" % request.POST.get('hostname'))
                    return cv.get_xml_conf(request)
                elif is_app('fsa.lcr') and request.POST.get('key_value') == "lcr.conf":
                    l.debug("hostname: %s (lcr.conf)" % request.POST.get('hostname'))
                    from fsa.lcr import views as lv
                    return lv.get_conf(request)
                else:
                    return sv.get(request)
            except Exception, e:
                l.error("Error import module: %s" % e)
    except Exception, e:
        l.error("Error generating confg %s" % e)
        return HttpResponseNotFound('<h1>Error generating config</h1>')
        