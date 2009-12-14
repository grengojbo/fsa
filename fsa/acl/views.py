# -*- coding: UTF-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from fsa.acl.models import FSAcl
from django.views.generic.list_detail import object_list
from sugar.views.decorators import render_to
from django.shortcuts import get_object_or_404      
import logging

l = logging.getLogger('fsa.acl.views')

__author__ = '$Author:$'
__revision__ = '$Revision:$'

# Create your views here.

@render_to('acl/acl.conf.xml')
def get(request):
    """ 
    reguest -- сами знаете что   
    """
    a = FSAcl.objects.get(server__name__exact=request.POST.get('hostname'), enabled=True)
    l.debug(request.POST.get('hostname'))
    return {'name':'acl.conf', 'xml_context':a.acl_val}

