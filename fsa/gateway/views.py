# -*- mode: python; coding: utf-8; -*-
from django.utils.translation import ugettext_lazy as _
from django.views.generic.list_detail import object_list
from sugar.views.decorators import render_to
from django.shortcuts import get_object_or_404
from lib.helpers import reverse
from fsa.gateway.models import SofiaGateway
from fsa.server.models import Server, SipProfile
import logging as l

__author__ = '$Author:$'
__revision__ = '$Revision:$'


@render_to('gateway/gateways.xml')
def get(request):
    """ 
    reguest -- сами знаете что
     -- список активных шлюзов
    """
    #print Server.objects.all()[0]
    #s = Server.objects.filter(name='grengo.colocall.net')
    s = Server.objects.filter(name=request.POST['hostname'])
    sg = get_object_or_404(SofiaGateway, enabled=True, server=s)
    #return {'es':Server.objects.get(name='linktel.com.ua')}
    return {'sg':sg}

@render_to('gateway/profile.xml')
def profile(request):
    """ 
    reguest -- сами знаете что
    return - список шлюзов для данного профиля
    """
    #print Server.objects.all()[0]
    l.debug('gateway profile: %s' % request.POST.get('profile'))
    sofia = SipProfile.objects.get(name = request.POST.get('profile'), enabled=True)
    return {'sofia':sofia}

