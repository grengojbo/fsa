# -*- mode: python; coding: utf-8; -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from fsa.server.models import Server
from fsa.lcr.models import Lcr
from django.views.generic.list_detail import object_list
from sugar.views.decorators import render_to
from django.shortcuts import get_object_or_404
import logging

l = logging.getLogger('fsa.lcr.views')

__author__ = '$Author: $'
__revision__ = '$Revision: $'

# Create your views here.

@render_to('directory/sip.xml')
def get(request):
    """ 
    reguest -- 
    """
    pass    

@render_to('lcr/lcr.conf.xml')    
def get_conf(request):
    """return lcr config file"""
    name = 'configuration'
    key_value = request.POST.get('key_value')
    es = get_object_or_404(Server, name=request.POST.get('hostname'))
    return request.Context({'name':name, 'key_value':key_value, 'es':es}).render_response('lcr/lcr.conf.xml')

