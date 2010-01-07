# -*- mode: python; coding: utf-8; -*-
from fsa.acl.models import FSAcl
from fsa.server.models import Server
import logging

l = logging.getLogger('fsa.acl.views')

__author__ = '$Author:$'
__revision__ = '$Revision:$'

# Create your views here.

def get(request):
    """ 
    reguest -- сами знаете что   
    """
    # TODO изменить на выбор acl для заданного сервера
    l.debug(request.POST.get('hostname'))
    #nls = FSAcl.objects.filter(acls__pk=2, enabled=True)
    nls = FSAcl.objects.filter(server_acl__name__exact=request.POST.get('hostname'),enabled=True)
    return request.Context({'name':'acl.conf', 'server':request.POST.get('hostname'), 'nls':nls}).render_response('acl/network_list.xml')
