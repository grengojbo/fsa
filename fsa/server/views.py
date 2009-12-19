# -*- mode: python; coding: utf-8; -*-
# Create your views here.

from django.utils.translation import ugettext_lazy as _
from django.views.generic.list_detail import object_list
#from sugar.views.decorators import render_to
from django.shortcuts import get_object_or_404
#from lib.helpers import reverse
from fsa.server.models import Server, SipProfile, Conf
import logging as l

#render_to('server/event_socket.conf.xml')
def get_event_socket(request):
    """ 
    reguest  -- сами знаете что
    """
    es = get_object_or_404(Server, name=request.POST.get('hostname'))
    #return {'es':es}
    return request.Context({'es':es}).render_response('server/event_socket.conf.xml')


#@render_to('server/sofia.conf.xml')
def get_sofia(request):
    """ 
    reguest -- сами знаете что
    возвращает конфиг для SIP
    """
    ss = SipProfile.objects.filter(enabled=True)
    #return {'ss':ss}
    return request.Context({'ss':ss}).render_response('server/sofia.conf.xml')
    

#@render_to('server/fs.xml')
def get(request):
    """
    xml по умолчанию 
    нет такой страницы и сервер берет конфиг из папки conf/autoload_config
    """
    try:
        ls = Conf.objects.get(server__name__exact=request.POST.get('hostname'), name__exact=request.POST.get('key_value'), enabled=True)
        name = 'configuration'
        key_value = request.POST.get('key_value')
        xml_context = ls.xml_conf
        l.debug("key_value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
    except Exception, e:
        key_value = name = 'result'
        xml_context = '<result status="not found" />'
        l.error('IS NOT key_value: %s' % request.POST.get('key_value'))
    #return {'name':name, 'xml_context':xml_context}
    return request.Context({'name':name, 'key_value':key_value, 'xml_context':xml_context}).render_response('server/fs.xml')
