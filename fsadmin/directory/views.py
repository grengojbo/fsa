# -*- coding: UTF-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from fsadmin.directory.models import Endpoint, FSGroup, SipRegistration
from fsadmin.directory.forms import EndpointForm
from django.views.generic.list_detail import object_list
from sugar.views.decorators import render_to, ajax_request
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from fsa.core import is_app 
import logging

l = logging.getLogger('fsadmin.directory.views')

__author__ = '$Author:$'
__revision__ = '$Revision:$'

# Create your views here.
xml_context = '<result status="not found" />'

@render_to('directory/sip.xml')
def profile(request):
    """ 
    reguest -- 
    """
    endpoint = Endpoint.objects.filter(enable=True,sip_profile__server__name=request.POST.get('domain'))
    # TODO доделать группы только этого пользователя
    gr = FSGroup.objects.all()
    return {'sd':endpoint,'groups':gr, 'domain':request.POST.get('domain')}

@render_to('server/fs.xml')
def get(request):
    """
    xml по умолчанию 
    нет такой страницы и сервер берет конфиг из папки conf/autoload_config
    """
    name = 'result'
    return {'name':name, 'xml_context':xml_context}

@render_to('directory/sip_reg.xml')
def set(request):
    """
    return
        sip - Endpoint onbject
        r - status ( 0 or 1 or 2 )
        domain - Domain Name 
        xml_context - Not Found
    """
    p = request.POST  
    if is_app('fsbilling.core'):
        fsb = True
    else:
        fsb = False
    try:
        e = Endpoint.objects.get(uid = p.get('user'), enable=True)
        r = SipRegistration.objects.sip_auth_nc(p,e)
        l.debug("uid: %s register: %d" % (p.get('user'), r))
        if r == 1:
            return {'sip':e, 'domain':p.get('domain'), 'fsb':fsb}
        else:
            return {'name': 'result', 'xml_context':xml_context}, 'server/fs.xml'
    except Endpoint.DoesNotExist:
        return {'name': 'result', 'xml_context':xml_context}, 'server/fs.xml'

@login_required
def directory_view(request):
    """
    Personal data of the user profile
    """
    pass
    
@login_required
@ajax_request
def new_endpoint(request):
    """
    Добавление нового номера
    """
    if not request.user.is_staff:
        return {'error': {'type': 403, 'message': 'Access denied'}}
    elif request.POST.get('new'):
        new_endpoint = Endpoint.objects.create_endpoint(request.user)
        return {'success': True, 'uid': new_endpoint.uid}
    else:
        return {'error': {'type': 400, 'message': 'Bad request'}}
        
@login_required
@render_to('directory/edit.html')
def directory_edit(request, object_id):
    """docstring for directory_edit"""
    endpoint = Endpoint.objects.get(pk = object_id, enable=True, accountcode = request.user)
    if request.method == "POST":
        form = EndpointForm(request.POST, instance=endpoint)
        if form.is_valid():
            form.save()
            #request.user.message_set.create(message=_("Your profile information has been updated successfully."))
    else:
        form = EndpointForm(instance=endpoint)
    data = { 'section': 'directory', 'form': form, 'e': endpoint, }
    return data