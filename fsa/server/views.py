# -*- mode: python; coding: utf-8; -*-
# Create your views here.

from django.utils.translation import ugettext_lazy as _
from django.views.generic.list_detail import object_list
#from sugar.views.decorators import render_to
from django.shortcuts import get_object_or_404
#from lib.helpers import reverse
from fsa.server.models import Server, SipProfile, Conf
from fsa.server.config import active_modules

import logging as l

#render_to('server/event_socket.conf.xml')
def get_event_socket(request):
    """ 
    reguest  -- сами знаете что
    """
    es = get_object_or_404(Server, name=request.POST.get('hostname'), enabled=True)
    #return {'es':es}
    return request.Context({'es':es}).render_response('server/event_socket.conf.xml')


#@render_to('server/sofia.conf.xml')
def get_sofia(request):
    """ 
    reguest -- сами знаете что
    возвращает конфиг для SIP
    """
    es = Server.objects.get(name=request.POST.get('hostname'), enabled=True)
    ss = SipProfile.objects.filter(server=es, enabled=True)
    return request.Context({'hostname':request.POST.get('hostname'), 'odbc_dsn':es.odbc_dsn, 'ss':ss, 's': es.options['SERVER'], 'l': es.options['LOGDEBUG']}).render_response('server/sofia.conf.xml')
    
def get_limit(request):
    """
    Файл конфигурации limit.conf
    подробнее смотреть http://wiki.freeswitch.org/wiki/Mod_limit
    """
    es = get_object_or_404(Server, name__exact=request.POST.get('hostname'), enabled=True)
    #l.debug("es.odbc_dsn %s" % (es.odbc_dsn))
    return request.Context({'name':request.POST.get('hostname'), 'odbc_dsn':es.odbc_dsn}).render_response('server/limit.conf.xml')
    

#@render_to('server/fs.xml')
def get(request):
    """
    xml по умолчанию 
    нет такой страницы и сервер берет конфиг из папки conf/autoload_config
    """
    try:
        conf_name = request.POST.get('key_value').split('.')[0]
        ls = Conf.objects.get(server__name__exact=request.POST.get('hostname'), name__exact=conf_name, enabled=True)
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

def post_switch(request):
    """переменные софт свича"""
    es = get_object_or_404(Server, name__exact=request.POST.get('hostname'), enabled=True)
    return request.Context({'name':request.POST.get('hostname'), 'odbc_dsn':es.odbc_dsn, 's': es.options['SERVER'], 'l': es.options['LOGDEBUG']}).render_response('server/switch.conf.xml')
    
def odbc_query(request):
    es = get_object_or_404(Server, name__exact=request.POST.get('hostname'), enabled=True)
    return request.Context({'name':request.POST.get('hostname'), 'odbc_dsn':es.odbc_dsn, 's': es.options['SERVER'], 'l': es.options['LOGDEBUG']}).render_response('server/odbc_query.conf.xml')
    
def post_modules(request):
    """
    загружаем модули
    """
    try:
        ml = Conf.objects.select_related('name').filter(server__name__exact=request.POST.get('hostname'), enabled=True)
        name = 'configuration'
        key_value = request.POST.get('key_value')
        l.debug("key_value %s hostname: %s" % (request.POST.get('key_value'), request.POST.get('hostname')))
        l.info(active_modules())
        return request.Context({'name':name, 'key_value':key_value, 'ml':ml, 'sml': active_modules()}).render_response('server/post_load_modules.conf.xml')
    except Exception, e:
        key_value = name = 'result'
        xml_context = '<result status="not found" />'
        l.error('IS NOT key_value: %s' % request.POST.get('key_value'))
        return request.Context({'name':name, 'key_value':key_value, 'xml_context':xml_context}).render_response('server/fs.xml')
