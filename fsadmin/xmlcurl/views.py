# -*- mode: python; coding: utf-8; -*-
from django.conf import settings
from django.http import HttpResponseNotFound
from sugar.views.decorators import render_to
from lib.http import HttpResponseRedirectView
from fsa.core import is_app
#from lib.helpers import reverse
#from django.utils.translation import ugettext_lazy as _
from fsa.server.models import Server, SipProfile
import logging

l = logging.getLogger('fsadmin.xmlcurl.views')

__author__ = '$Author:$'
__revision__ = '$Revision:$'

def get(request):
    """ 
    reguest -- 
    """
    # TODO только зарегистрированый FS
    try:
        l.debug("post: %s" % request.POST)
        if request.POST['section'] == "configuration":
            try:
                # TODO добавить загрузку конфигурации lcr.conf
                from fsa.server import views as sv
                if (request.POST.get('key_value') == "event_socket.conf"):
                    l.debug("hostname: %s" % request.POST.get('hostname'))
                    #return HttpResponseRedirectView(sv.get_event_socket, request)
                    return sv.get_event_socket(request)
                elif (request.POST['key_value'] == "sofia.conf"):
                    l.debug("hostname: %s" % request.POST.get('hostname'))
                    return sv.get_sofia(request)
                elif (request.POST['key_value'] == "cdr_csv.conf"):
                    from fsa.cdr import views as cv
                    l.debug("key_ value cdr_csv.conf hostname: %s" % request.POST.get('hostname'))
                    return cv.get_csv_conf(request)
                elif (request.POST['key_value'] == "xml_cdr.conf"):
                    from fsa.cdr import views as cv
                    l.debug("key_ value xml_cdr.conf hostname: %s" % request.POST.get('hostname'))
                    return cv.get_xml_conf(request)
                elif (request.POST['key_value'] == "acl.conf"):
                    from fsa.acl import views as av
                    l.debug("key_ value acl.conf hostname: %s" % request.POST.get('hostname'))
                    return av.get(request)
                elif is_app('fsadmin.lcr') and request.POST.get('key_value') == "lcr.conf":
                    l.debug("hostname: %s (lcr.conf)" % request.POST.get('hostname'))
                    from fsadmin.lcr import views as lv
                    return lv.get_conf(request)
                elif is_app('fsbilling.core') and request.POST.get('key_value') == "nibblebill.conf":
                    l.debug("hostname: %s (nibblebill.conf)" % request.POST.get('hostname'))
                    from fsbilling.core import views as cv
                    return cv.get_conf(request)
                else:
                    l.error('IS NOT key_value: %s' % request.POST.get('key_value'))
                    #return HttpResponseNotFound('<h1>IS NOT key_value: %s</h1>' % request.POST['key_value'])
                    return sv.get(request)
            except Exception, e:
                l.error("Error import module: %s" % e)
        elif request.POST['section'] == "dialplan":
            l.debug("got post: key_value %s " % request.POST['key_value'])
        elif request.POST['section'] == "directory":
            # TODO Add module dialplan
            l.debug("got post: key_value %s section: directory" % request.POST['key_value'])
            try:
                from fsa.directory import views as d
                from fsa.gateway import views as gw
                from fsa.server import views as sv
                if request.POST.get('profile') and request.POST['purpose'] == 'gateways':
                    # TODO сейчас выдает пустушку но если раскоментировать то будет выдавать список шлюзов
                    # но тогда наверное нужно убрать из server/sip_profile.xml секцию gateways  
                    # но зачем это надо непойму и так они подгружаются через server/sip_profile
                    #return gw.profile(request)
                    return sv.get(request)
                elif request.POST.get('purpose') == 'network-list':
                    # TODO так и непонял нах оно надо в доке пишут
                    # This last post is regarding mod_sofia asking for users with cidr = attributes for adding them to the acls.
                    return sv.get(request)
                elif request.POST.get('sip_auth_nc'):
                    return d.set(request)
                else:
                    return d.get(request)
            except Exception, e:
                l.error("Error import module: %s" % e)
        else:
            l.debug("IS NOT section %s " % request.POST.get('section'))
            return HttpResponseNotFound('<h1>section %s</h1>' % request.POST.get('section'))

    except Exception, e:
        l.error("Error generating confg %s" % e)
        return HttpResponseNotFound('<h1>Error generating config</h1>')

