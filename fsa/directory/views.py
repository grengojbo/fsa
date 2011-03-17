# -*- mode: python; coding: utf-8; -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from fsa.directory.models import Endpoint, FSGroup
from fsa.server.models import Server, SipProfile, Conf
from fsa.directory.forms import EndpointForm
import keyedcache
from django.views.generic.list_detail import object_list
from sugar.views.decorators import render_to, ajax_request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.shortcuts import redirect
from fsa.core import is_app
import logging

log = logging.getLogger('fsa.directory.views')

__author__ = '$Author:$'
__revision__ = '$Revision:$'

# Create your views here.
xml_context = '<result status="not found" />'

#@render_to('directory/sip.xml')
def profile(request):
    """
    reguest --
    """
    endpoint = Endpoint.objects.filter(enable=True,sip_profile__server__name=request.POST.get('domain'))
    # TODO доделать группы только этого пользователя
    gr = FSGroup.objects.all()
    return {'sd':endpoint,'groups':gr, 'domain':request.POST.get('domain')}

#@render_to('server/fs.xml')
def get(request):
    """
    xml по умолчанию
    нет такой страницы и сервер берет конфиг из папки conf/autoload_config
    """
    name = 'result'
    return {'name':name, 'xml_context':xml_context}

def set(request):
    """
    Register Endpoint
    return
        sip - Endpoint onbject
        r - status ( 0 or 1 or 2 )
        domain - Domain Name
        xml_context - Not Found
    """
    p = request.POST
    key_value = name = 'result'
    xml_context = '<result status="not found" />'
    #TODO add caching
    try:
        key_value = p.get('user')
        if p.get('action') == 'sip_auth':
            e = Endpoint.objects.get(uid__exact = p.get('user'), enable=True, sip_profile__name__exact=p.get('sip_profile'))
            if is_app('fsb.tariff'):
                #from fsb.tariff.models import TariffPlan
                tariff = True
            else:
                tariff = False
            return request.Context({'name':name, 'key_value':key_value, 'sip':e, 'tariff':tariff, 'domain':p.get('domain')}).render_response('directory/sip_reg.xml')
        elif p.get('action') == 'message-count':
            e = Endpoint.objects.get(uid = p.get('user'), enable=True)
            if is_app('fsb.tariff'):
                #from fsb.tariff.models import TariffPlan
                tariff = True
            else:
                tariff = False
            return request.Context({'name':name, 'key_value':key_value, 'sip':e, 'tariff':tariff, 'domain':p.get('domain')}).render_response('directory/sip_reg.xml')
        else:
            return request.Context({'name':name, 'key_value':key_value, 'xml_context':xml_context}).render_response('server/fs.xml')
    except Endpoint.DoesNotExist:
        return request.Context({'name':name, 'key_value':key_value, 'xml_context':xml_context}).render_response('server/fs.xml')

##        r = SipRegistration.objects.sip_auth_nc(p,e)
##        l.debug("uid: %s register: %d" % (p.get('user'), r))
##        if r == 1:
##            #return {'sip':e, 'domain':p.get('domain'), 'fsb':fsb}
##            key_value = p.get('user')
##            return request.Context({'name':name, 'key_value':key_value, 'sip':e, 'domain':p.get('domain'), 'fsb':fsb }).render_response('directory/sip_reg.xml')
##        else:
##

def gw(request):
    p = request.POST
    key_value = name = 'result'
    xml_context = '<result status="not found" />'
    key_caches = "directory:gw:{0}".format(p.get('profile'))
    try:
        sofia = keyedcache.cache_get(key_caches)
        return request.Context({'hostname':request.POST.get('hostname'), 'sofia':sofia}).render_response('directory/gw.xml')
    except keyedcache.NotCachedError, nce:
        try:
            sofia = SipProfile.objects.get(enabled=True, name__exact=p.get('profile'))
            keyedcache.cache_set(key_caches, value=sofia)
            return request.Context({'hostname':request.POST.get('hostname'), 'sofia':sofia}).render_response('directory/gw.xml')
        except:
            #SipProfile.DoesNotExist:
            return request.Context({'name':name, 'key_value':key_value, 'xml_context':xml_context}).render_response('server/fs.xml')
        return request.Context({'name':name, 'key_value':key_value, 'xml_context':xml_context}).render_response('server/fs.xml')

def gateways(request):
    p = request.POST
    key_value = name = 'result'
    xml_context = '<result status="not found" />'
    #es = Server.objects.get(name=request.POST.get('hostname'), enabled=True)
    #sofia = SipProfile.objects.get(server=es, enabled=True, name=request.POST.get('profile'))
    #return request.Context({'hostname':request.POST.get('hostname'), 'server':es, 'sofia':sofia, 's': es.options['SERVER']}).render_response('gateway/profile.xml')

    try:
        es = Server.objects.get(name=request.POST.get('hostname'), enabled=True)
        sofia = SipProfile.objects.get(server=es, enabled=True, name=request.POST.get('profile'))
        return request.Context({'hostname':request.POST.get('hostname'), 'server':es, 'sofia':sofia, 's': es.options['SERVER']}).render_response('gateway/profile.xml')
    except:
        return request.Context({'name':name, 'key_value':key_value, 'xml_context':xml_context}).render_response('server/fs.xml')

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
def edit(request, object_id, template_name='directory/edit.html', success_url='profile_overview', extra_context=None, **kwargs):
    """Chenge parameters Endpoint"""
    # TODO: add test
    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value

    endpoint = get_object_or_404(Endpoint, uid__exact=object_id, enable=True, accountcode=request.user)
    if request.method == "POST":
        form = EndpointForm(request, instance=endpoint, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            #request.user.message_set.create(message=_("Your profile information has been updated successfully."))
            data = form.cleaned_data
            log.debug('form valid {0}'.format(data))
            return redirect(success_url)
    else:
        form = EndpointForm(request, instance=endpoint)
    data = {'form': form, 'e': endpoint, 'subsection': 'directory', 'section': 'profile', 'ip':request.META['REMOTE_ADDR']}
    #data = { 'e': endpoint, 'subsection': 'directory', 'section': 'profile', 'ip':request.META['REMOTE_ADDR']}
    return render_to_response(template_name, data, context_instance=context)