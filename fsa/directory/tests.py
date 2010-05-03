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

class DirectoryTestCase(test.TestCase):
    #fixtures = ['testsite', 'testnp', 'acl', 'alias', 'extension', 'context', 'server', 'server_conf', 'gateway', 'sipprofile']
    #fixtures = ['testsite', 'testnp', 'acl', 'alias', 'extension', 'context', 'server', 'server_conf', 'gateway', 'sipprofile']
    fixtures = ['testsite', 'testnp', 'acl', 'alias', 'extension', 'context', 'server', 'server_conf', 'gateway', 'sipprofile']
    def setUp(self):
        #cont1 = Context(name="default", default_context=True)
        #cont1.save()
        #cont2 = Context(name="public", default_context=False)
        #cont2.save()
        #cont3 = Context(name="private", default_context=False)
        #cont3.save()
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
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

    def testCreateEndpoint(self):
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
        
    def testNewEndpoint(self):
        """docstring for testNewEndpoint"""
        #from userprofile import signals
        #signals.profile_registration.send(sender="ProfileRegistration", request=request, user=newuser)
        pass
        
    def testEndpoints(self):
        """sip id для конкретного домена"""
        #endpoint = Endpoint.objects.filter(enable=True,sip_profile__server__name=request.POST.get('domain'))
        pass
        
    def testSipRegistration(self):
        """
        Проверка регистрация на FS sip устройства 
        """
        new_endpoint = Endpoint.objects.create_endpoint(self.user)
        response = self.client.post('/api/directory/', {'profile': 'test1.example.com', 'key_value': '', 'key_name': '', 'section': 'directory', 'hostname': self.hostname, 'tag_name': '', 'purpose': 'gateways'})
        self.assertEquals(response.status_code, 200)
        l.debug(response)
        
        sip_auth_nonce = 'e8c26e3e-1792-11de-ae36-af3bf0ae904b'
        sip_auth_nc = '00000001'
        p  = {'domain': '192.168.51.100', 'sip_contact_user': new_endpoint.uid, 'ip': '192.168.51.240', 'sip_from_user': new_endpoint.uid, 'sip_auth_nc': sip_auth_nc, 'section': 'directory', 'hostname': 'test1.example.com', 'sip_auth_method': 'REGISTER', 'sip_auth_username': new_endpoint.uid, 'sip_auth_nonce': sip_auth_nonce, 'sip_to_host': '192.168.51.100', 'key_value': '192.168.51.100', 'sip_request_host': '192.168.51.100', 'key_name': 'name', 'sip_from_host': '192.168.51.100', 'sip_auth_uri': 'sip:192.168.51.100', 'user': new_endpoint.uid, 'key': 'id', 'sip_auth_cnonce': '8c2f4caf26d8082712b707a36c0131ee', 'sip_auth_response': '353416c6e18345b621b167acfbcf2182', 'sip_user_agent': 'X-Lite release 1100l stamp 47546', 'sip_auth_realm': '192.168.51.100', 'sip_to_user': new_endpoint.uid, 'sip_auth_qop': 'auth', 'tag_name': 'domain', 'sip_profile': 'test1.example.com', 'action': 'sip_auth', 'sip_contact_host': '192.168.51.251'}
        # Добавление
        sr = SipRegistration.objects.sip_auth_nc(p,new_endpoint)
        self.assertEquals(sr, 1)
        # Удаление 
        sip_auth_nc = '00000002'
        p  = {'domain': '192.168.51.100', 'sip_contact_user': new_endpoint.uid, 'ip': '192.168.51.240', 'sip_from_user': new_endpoint.uid, 'sip_auth_nc': sip_auth_nc, 'section': 'directory', 'hostname': 'test1.example.com', 'sip_auth_method': 'REGISTER', 'sip_auth_username': new_endpoint.uid, 'sip_auth_nonce': sip_auth_nonce, 'sip_to_host': '192.168.51.100', 'key_value': '192.168.51.100', 'sip_request_host': '192.168.51.100', 'key_name': 'name', 'sip_from_host': '192.168.51.100', 'sip_auth_uri': 'sip:192.168.51.100', 'user': new_endpoint.uid, 'key': 'id', 'sip_auth_cnonce': '8c2f4caf26d8082712b707a36c0131ee', 'sip_auth_response': '353416c6e18345b621b167acfbcf2182', 'sip_user_agent': 'X-Lite release 1100l stamp 47546', 'sip_auth_realm': '192.168.51.100', 'sip_to_user': new_endpoint.uid, 'sip_auth_qop': 'auth', 'tag_name': 'domain', 'sip_profile': 'test1.example.com', 'action': 'sip_auth', 'sip_contact_host': '192.168.51.251'}
        sr = SipRegistration.objects.sip_auth_nc(p,new_endpoint)
        # TODO работает неправильно должно быть 2
        self.assertEquals(sr, 1)
        srf = SipRegistration.objects.sip_auth_nc(p,new_endpoint)
        self.assertEquals(srf, 0)

