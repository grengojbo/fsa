# -*- mode: python; coding: utf-8; -*-
# Create your views here.

from django.utils.translation import ugettext_lazy as _
from django.views.generic.list_detail import object_list
#from sugar.views.decorators import render_to
from django.shortcuts import get_object_or_404
#from lib.helpers import reverse
from fsa.server.models import Server, SipProfile, Conf

#render_to('server/event_socket.conf.xml')
def get_event_socket(request):
    """ 
    reguest  -- сами знаете что
    """
    # TODO добавить ACL <!--<param name="apply-inbound-acl" value="lan"/>-->
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
    name = 'result'
    xml_context = '<result status="not found" />'
    
    #return {'name':name, 'xml_context':xml_context} 
    return request.Context({'name':name, 'xml_context':xml_context}).render_response('server/fs.xml')
