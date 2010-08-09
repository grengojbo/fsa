# -*- mode: python; coding: utf-8; -*-
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

__author__ = '$Author$'
__revision__ = '$Revision$'

import unittest
from django import test
from django.test.client import Client
from django.contrib.auth.models import User
from fsa.directory.models import Endpoint, SipRegistration
from fsa.dialplan.models import Context
import logging as l
from django.contrib.sites.models import Site
from fsa.server.models import Server, SipProfile, Conf
from fsa.core import is_app
import urllib, base64
import simplejson
import keyedcache
from decimal import Decimal

class DirectoryTestCase(test.TestCase):
    #fixtures = ['testsite', 'testnp', 'acl', 'alias', 'extension', 'context', 'server', 'server_conf', 'gateway', 'sipprofile']
    #fixtures = ['testsite', 'testnp', 'acl', 'alias', 'extension', 'context', 'server', 'server_conf', 'gateway', 'sipprofile']
    if is_app('fsb.tariff'):
        fixtures = ['testsite', 'testnp', 'acl', 'alias', 'extension', 'context', 'server', 'server_conf', 'test_gateway', 'sipprofile', 'tariffplan']
    else:
        fixtures = ['testsite', 'testnp', 'acl', 'alias', 'extension', 'context', 'server', 'server_conf', 'test_gateway', 'sipprofile']
    
    def setUp(self):
        #cont1 = Context(name="default", default_context=True)
        #cont1.save()
        #cont2 = Context(name="public", default_context=False)
        #cont2.save()
        #cont3 = Context(name="private", default_context=False)
        #cont3.save()
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        #self.user = User.objects.create_user('admin', 'admin@world.com', 'admin')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.is_active = True
        #self.user.user_permissions.add(permission)
        self.user.save()
        self.auth_string = 'Basic %s' % base64.encodestring('test:test').rstrip()
        # Every test needs a client.
        self.client = Client()
        #self.uid = 3000
        #self.p = "123456"
        #self.effective_caller_id_name = self.uid
        #self.enable = True
        self.hostname = 'test1.example.com'
        self.hostip = '192.168.51.100'
        self.domainname = '192.168.51.100'
        self.xml_context = '<result status="not found" />'
        self.site = Site.objects.get(pk=1)

    def test01CreateEndpoint(self):
        """
        Добавляем sip id для пользователя
        """
        new_endpoint = Endpoint.objects.create_endpoint(self.user)
        self.assertEquals(new_endpoint.accountcode.pk, 1)
        self.assertEquals(self.user.username, 'test')
        self.assertEquals(self.user.is_active, True)
        self.assertEquals(new_endpoint.is_registered, False)
        self.assertEquals(new_endpoint.uid, '1003')
        new_endpoint = Endpoint.objects.create_endpoint(self.user, '4433')
        self.assertEquals(new_endpoint.uid, '4433')
        
        #from userprofile import signals
        #signals.profile_registration.send(sender="ProfileRegistration", request=request, user=newuser)

        #endpoint = Endpoint.objects.filter(enable=True,sip_profile__server__name=request.POST.get('domain'))
        
        #'action': 'message-count',
        #{'key': 'id', 'FreeSWITCH-IPv4': '95.67.67.187', 'key_value': '089.com.ua', 'FreeSWITCH-IPv6': '::1',
        #'Event-Date-Local': '2010-08-06 00:56:12', 'Event-Calling-Line-Number': '1242', 'key_name': 'name', 
        #'section': 'directory', 'hostname': 'gw', 'Event-Date-GMT': 'Thu, 05 Aug 2010 21:56:12 GMT', 'domain': '089.com.ua',
        #'Event-Name': 'GENERAL', 'tag_name': 'domain', 'FreeSWITCH-Hostname': 'gw', 'Event-Date-Timestamp': '1281045372124452',
        #'user': '380895001000', 'Event-Calling-Function': 'resolve_id', 'action': 'message-count',
        #'Event-Calling-File': 'mod_voicemail.c', 'Core-UUID': '49ce5823-63b8-469f-9720-d9a7850c39bb'}
        
    def test02SipRegistration(self):
        """
        Проверка регистрация на FS sip устройства 
        """
        # directory gateway
        new_endpoint = Endpoint.objects.create_endpoint(self.user)
        response = self.client.post('/api/directory/', {'profile': 'internal', 'key_value': '', 'key_name': '', 'section': 'directory', 'hostname': self.hostname, 'tag_name': '', 'purpose': 'gateways'}, HTTP_AUTHORIZATION=self.auth_string)
        self.assertEquals(response.status_code, 200)
        #l.debug(response)
        #es = Server.objects.get(name=self.hostname, enabled=True)
        sofia = SipProfile.objects.get(enabled=True, name__exact='internal')
        sofia.sites.add(self.site)
        sofia.save()
        self.assertEquals(sofia.sites.all().count(), 1)
        response = self.client.post('/api/directory/', {'profile': 'internal', 'key_value': '', 'key_name': '', 'section': 'directory', 'hostname': self.hostname, 'tag_name': '', 'purpose': 'gateways'}, HTTP_AUTHORIZATION=self.auth_string)
        self.assertEquals(response.status_code, 200)
        #l.debug(response)
        response = self.client.post('/api/directory/', {'profile': 'internal', 'key_value': '', 'key_name': '', 'section': 'directory', 'hostname': self.hostname, 'tag_name': '', 'purpose': 'gateways'}, HTTP_AUTHORIZATION=self.auth_string)
        self.assertEquals(response.status_code, 200)
        #l.debug(response)
        
        #directory network-list
        response = self.client.post('/api/directory/', {'key_value': '089.com.ua', 'key_name': 'name', 'section': 'directory', 'hostname': self.hostname, 'domain': '089.com.ua', 'tag_name': 'domain', 'purpose': 'network-list'}, HTTP_AUTHORIZATION=self.auth_string)
        self.assertEquals(response.status_code, 200)
        #l.debug(response)
        
        #sip_auth_nonce = 'e8c26e3e-1792-11de-ae36-af3bf0ae904b'
        #sip_auth_nc = '00000001'
        #response = self.client.post('/api/directory/', { 'hostname': 'test1.example.com', 'sip_profile': 'internal', 'section': 'directory', 'tag_name': 'domain', 'key_name': 'name', 
               #'key_value': '192.168.51.100', 'action': 'sip_auth',
              #'sip_user_agent': 'X-Lite release 1100l stamp 47546', 'sip_auth_username': new_endpoint.uid, 'sip_auth_realm': '192.168.51.100', 'sip_auth_nonce': sip_auth_nonce, 
              #'sip_contact_user': new_endpoint.uid, 'sip_contact_host': '192.168.51.251', 'sip_to_user': new_endpoint.uid, 'sip_to_host': '192.168.51.100', 
              #'sip_from_user': new_endpoint.uid, 'sip_from_host': '192.168.51.100', 'sip_auth_uri': 'sip:192.168.51.100', 'sip_request_host': '192.168.51.100',
              #'sip_auth_qop': 'auth', 'sip_auth_cnonce': '8c2f4caf26d8082712b707a36c0131ee', 'sip_auth_nc': sip_auth_nc,   'sip_auth_method': 'REGISTER', 
              #'domain': '192.168.51.100', 'key': 'id', 'user': new_endpoint.uid, 'ip': '192.168.51.240', 'sip_auth_response': 'aca561ab4fc8a886fc7852165333bbfb'})
        #self.assertEquals(response.status_code, 200)
        #l.debug(response)
        # Добавление
         
    def test03ApiBilling(self):
        """
        Проверка регистрация на FS sip устройства 
        """
        # directory gateway
        phone = '1003'
        gw = 'ukrtelecomin'
        
        new_endpoint = Endpoint.objects.create_endpoint(self.user)
        self.assertEquals(new_endpoint.uid, phone)
        self.assertEquals(new_endpoint.phone_type, 'S')
        new_endpoint.phone_type = 'I'
        new_endpoint.site = self.site
        new_endpoint.phone_alias = 'demo-ivr'
        new_endpoint.save()
        self.assertEquals(new_endpoint.phone_type, 'I')
        endpoint = Endpoint.objects.get(uid__exact=phone, enable=True)
        response = self.client.get('/api/billing/in/{0}/{1}/'.format(gw, phone))
        self.assertEquals(response.status_code, 401)
        response = self.client.get('/api/billing/in/{0}/{1}/'.format(gw, phone), HTTP_AUTHORIZATION=self.auth_string)
        self.assertEquals(response.status_code, 200)
        res = simplejson.loads(response.content.encode('UTF-8'))
        self.assertEquals(Decimal(res.get('lcr_price')), Decimal("0.18"))
        
        gw = 'testgw'
        response = self.client.get('/api/billing/in/{0}/{1}/'.format(gw, phone), HTTP_AUTHORIZATION=self.auth_string)
        self.assertEquals(response.status_code, 200)
        res = simplejson.loads(response.content.encode('UTF-8'))
        self.assertEquals(Decimal(res.get('lcr_price')), Decimal("0.21"))
        self.assertEquals(res.get('endpoint').get('phone_type'), 'I')
        self.assertEquals(res.get('endpoint').get('phone_alias'), 'demo-ivr')
        self.assertEquals(res.get('endpoint').get('accountcode').get('username'), 'test')
        self.assertEquals(res.get('endpoint').get('site').get('name'), 'test1.example.com')
        self.assertEquals(res.get('endpoint').get('zrtp'), False)
        
        #l.debug(res)
        

##        sr = SipRegistration.objects.sip_auth_nc(p,new_endpoint)
##        self.assertEquals(sr, 1)
##        # Удаление 
##        sip_auth_nc = '00000002'
##        p  = {'domain': '192.168.51.100', 'sip_contact_user': new_endpoint.uid, 'ip': '192.168.51.240', 'sip_from_user': new_endpoint.uid, 'sip_auth_nc': sip_auth_nc, 'section': 'directory', 'hostname': 'test1.example.com', 'sip_auth_method': 'REGISTER', 'sip_auth_username': new_endpoint.uid, 'sip_auth_nonce': sip_auth_nonce, 'sip_to_host': '192.168.51.100', 'key_value': '192.168.51.100', 'sip_request_host': '192.168.51.100', 'key_name': 'name', 'sip_from_host': '192.168.51.100', 'sip_auth_uri': 'sip:192.168.51.100', 'user': new_endpoint.uid, 'key': 'id', 'sip_auth_cnonce': '8c2f4caf26d8082712b707a36c0131ee', 'sip_auth_response': '353416c6e18345b621b167acfbcf2182', 'sip_user_agent': 'X-Lite release 1100l stamp 47546', 'sip_auth_realm': '192.168.51.100', 'sip_to_user': new_endpoint.uid, 'sip_auth_qop': 'auth', 'tag_name': 'domain', 'sip_profile': 'test1.example.com', 'action': 'sip_auth', 'sip_contact_host': '192.168.51.251'}
##        sr = SipRegistration.objects.sip_auth_nc(p,new_endpoint)
##        # TODO работает неправильно должно быть 2
##        self.assertEquals(sr, 1)
##        srf = SipRegistration.objects.sip_auth_nc(p,new_endpoint)
##        self.assertEquals(srf, 0)

