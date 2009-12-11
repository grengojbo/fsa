# -*- coding: UTF-8 -*-
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

__author__ = '$Author:$'
__revision__ = '$Revision:$'

#from django.test import TestCase
import unittest
from django import test
from django.test.client import Client
from django.contrib.auth.models import User
#from fsadmin.directory.models import Endpoint, SipRegistration
#from fsadmin.dialplan.models import Context
import logging as l

#class SimpleTest(unittest.TestCase):
class XmlCurlTestCase(test.TestCase):
    fixtures = ['testsite', 'alias', 'context', 'extension', 'server', 'acl', 'gateway', 'fsgroup', 'sipprofile', 'testnp', 'testendpoint', 'testcdr']
    def setUp(self):
        # Every test needs a client.
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.hostname = 'test1.example.com'
        self.hostip = '192.168.51.100'
        self.domainname = '192.168.51.100'
        self.xml_context = '<result status="not found" />'
        self.client = Client()

    def testConfiguration(self):
        """
        Test Configuration section
        """
        # Issue a GET request.
        ##response = self.client.get('/customer/details/')
        ## Check that the response is 200 OK.
        ##self.failUnlessEqual(response.status_code, 200)
        # Check that the rendered context contains 5 customers.
        ##self.failUnlessEqual(len(response.context['customers']), 5)
        response = self.client.post('/xmlcurl/get/', {'key_value': 'event_socket.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response.status_code, 200)
        response1 = self.client.post('/xmlcurl/get/', {'key_value': 'xml_cdr.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response1.status_code, 200)
        
        # TODO: is not hostname
        #response1a = self.client.post('/xmlcurl/get/', {'key_value': 'xml_cdr.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': 'error.example.com', 'tag_name': 'configuration'})
        #self.assertEquals(response1a.status_code, 200)

        response2 = self.client.post('/xmlcurl/get/', {'key_value': 'sofia.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response2.status_code, 200)
        #l.debug("sofia.conf >>> %s " % response2.context['ss'])
        #self.assertEquals(response2.context['sofia.server.sql_name'], 'fsmysql') 
        
        #response = self.client.post('/xmlcurl/get/', {'key_value': 'conference.conf', 'presence': 'true', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        #self.failUnlessEqual(response.status_code, 200)
        #response = self.client.post('/xmlcurl/get/', {'key_value': 'fifo.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        #self.failUnlessEqual(response.status_code, 200)
        #response = self.client.post('/xmlcurl/get/', {'key_value': 'voicemail.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        #self.failUnlessEqual(response.status_code, 200)
        #response = self.client.post('/xmlcurl/get/', {'key_value': 'limit.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        #self.failUnlessEqual(response.status_code, 200)
        
        response = self.client.post('/xmlcurl/get/', {'key_value': 'local_stream.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['xml_context'], self.xml_context)
        
        ##{'key_value': 'spidermonkey.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': 'grengo.colocall.net', 'tag_name': 'configuration'}
        ##{'key_value': 'lua.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': 'grengo.colocall.net', 'tag_name': 'configuration'}
        ##{'key_value': 'post_load_modules.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': 'grengo.colocall.net', 'tag_name': 'configuration'}
        
        response = self.client.post('/xmlcurl/get/', {'key_value': 'acl.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response.status_code, 200)
        
        response = self.client.post('/xmlcurl/get/', {'key_value': 'lcr.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response.status_code, 200)
        
        response = self.client.post('/xmlcurl/get/', {'key_value': 'nibblebill.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response.status_code, 200)
        print response.content
        
        #response = self.client.post('/xmlcurl/get/', {'key_value': 'event_socket.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': 'grengo.colocall.net', 'tag_name': 'configuration'})
        #self.failUnlessEqual(response.status_code, 200)
        ##{'key_value': 'post_load_switch.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': 'grengo.colocall.net', 'tag_name': 'configuration'}
        #response = self.client.post('/xmlcurl/get/', {'key_value': 'switch.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': 'grengo.colocall.net', 'tag_name': 'configuration'})
        #self.failUnlessEqual(response.status_code, 200)

    def testDirectory(self):
        """
        Test Directory section
        """
        
        response = self.client.post('/xmlcurl/get/', {'profile': 'test1.example.com', 'key_value': '', 'key_name': '', 'section': 'directory', 'hostname': self.hostname, 'tag_name': '', 'purpose': 'gateways'})
        self.assertEquals(response.status_code, 200)
        
        response = self.client.post('/xmlcurl/get/', {'key_value': self.hostip, 'key_name': 'name', 'section': 'directory', 'hostname': self.hostname, 'domain': self.domainname, 'tag_name': 'domain', 'purpose': 'network-list'})
        self.assertEquals(response.status_code, 200)
        
        # регистрация
        # нет такого номера
        curuser = '2000002'
        curip= '177.122.12.196'
        sip_auth_nonce = 'e8c26e3e-1792-11de-ae36-af3bf0ae904b'
        response = self.client.post('/xmlcurl/get/', {'domain': self.domainname, 'Event-Date-Local': '2009-04-27 00:11:21', 'sip_contact_user': curuser, 'ip': curip, 'Event-Calling-Function': 'sofia_reg_parse_auth', 'Event-Date-GMT': 'Sun, 26 Apr 2009 21:11:21 GMT', 'sip_from_user': curuser, 'sip_auth_nc': '00000001', 'Event-Calling-Line-Number': '1608', 'section': 'directory', 'hostname': self.hostname, 'sip_auth_method': 'REGISTER', 'sip_auth_username': curuser, 'sip_auth_nonce': sip_auth_nonce, 'sip_contact_host': curip, 'sip_to_host': self.hostip, 'key_value': self.hostip, 'sip_request_host': self.hostip, 'key_name': 'name', 'Event-Date-Timestamp': '1240780281529899', 'sip_from_host': self.hostip, 'Event-Name': 'REQUEST_PARAMS', 'sip_auth_uri': 'sip:100.100.100.100', 'user': curuser, 'key': 'id', 'sip_auth_cnonce': 'WPywjtf8PgNdUIrezgjdg6mM-Rw-2M5x', 'sip_auth_response': '4b604606a06e9f83f5e76f9b9f66661e', 'FreeSWITCH-IPv4': self.hostip, 'sip_user_agent': 'Telephone 0.13.3', 'FreeSWITCH-IPv6': '::1', 'sip_auth_realm': self.hostip, 'sip_profile': 'test1.example.com', 'sip_auth_qop': 'auth', 'tag_name': 'domain', 'FreeSWITCH-Hostname': self.hostname, 'sip_to_user': curuser, 'action': 'sip_auth', 'Event-Calling-File': 'sofia_reg.c', 'Core-UUID': 'f46e9270-32a5-11de-bb04-791dda701640'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['xml_context'], '<result status="not found" />')
        # все окейно
        curuser = '2000001'
        curip= '177.122.12.196'
        sip_auth_nonce = 'e8c26e3e-1792-11de-ae36-af3bf0ae904b'
        response = self.client.post('/xmlcurl/get/', {'domain': self.domainname, 'Event-Date-Local': '2009-04-27 00:11:21', 'sip_contact_user': curuser, 'ip': curip, 'Event-Calling-Function': 'sofia_reg_parse_auth', 'Event-Date-GMT': 'Sun, 26 Apr 2009 21:11:21 GMT', 'sip_from_user': curuser, 'sip_auth_nc': '00000001', 'Event-Calling-Line-Number': '1608', 'section': 'directory', 'hostname': self.hostname, 'sip_auth_method': 'REGISTER', 'sip_auth_username': curuser, 'sip_auth_nonce': sip_auth_nonce, 'sip_contact_host': curip, 'sip_to_host': self.hostip, 'key_value': self.hostip, 'sip_request_host': self.hostip, 'key_name': 'name', 'Event-Date-Timestamp': '1240780281529899', 'sip_from_host': self.hostip, 'Event-Name': 'REQUEST_PARAMS', 'sip_auth_uri': 'sip:100.100.100.100', 'user': curuser, 'key': 'id', 'sip_auth_cnonce': 'WPywjtf8PgNdUIrezgjdg6mM-Rw-2M5x', 'sip_auth_response': '4b604606a06e9f83f5e76f9b9f66661e', 'FreeSWITCH-IPv4': self.hostip, 'sip_user_agent': 'Telephone 0.13.3', 'FreeSWITCH-IPv6': '::1', 'sip_auth_realm': self.hostip, 'sip_profile': 'test1.example.com', 'sip_auth_qop': 'auth', 'tag_name': 'domain', 'FreeSWITCH-Hostname': self.hostname, 'sip_to_user': curuser, 'action': 'sip_auth', 'Event-Calling-File': 'sofia_reg.c', 'Core-UUID': 'f46e9270-32a5-11de-bb04-791dda701640'})
        self.assertEquals(response.status_code, 200)
        # TODO ошибка KeyError: 'domain'
        #self.assertEquals(response.context['domain'], self.domainname)
        
        #print response.content
        #print response.context['domain']
        # print " \n"
        # print " \n"
        # акаунт есть но неактивный
        curuser = '2000000'
        curip= '177.122.12.196'
        sip_auth_nonce = 'e8c26e3e-1792-11de-ae36-af3bf0ae904b'
        response = self.client.post('/xmlcurl/get/', {'domain': self.domainname, 'Event-Date-Local': '2009-04-27 00:11:21', 'sip_contact_user': curuser, 'ip': curip, 'Event-Calling-Function': 'sofia_reg_parse_auth', 'Event-Date-GMT': 'Sun, 26 Apr 2009 21:11:21 GMT', 'sip_from_user': curuser, 'sip_auth_nc': '00000001', 'Event-Calling-Line-Number': '1608', 'section': 'directory', 'hostname': self.hostname, 'sip_auth_method': 'REGISTER', 'sip_auth_username': curuser, 'sip_auth_nonce': sip_auth_nonce, 'sip_contact_host': curip, 'sip_to_host': self.hostip, 'key_value': self.hostip, 'sip_request_host': self.hostip, 'key_name': 'name', 'Event-Date-Timestamp': '1240780281529899', 'sip_from_host': self.hostip, 'Event-Name': 'REQUEST_PARAMS', 'sip_auth_uri': 'sip:100.100.100.100', 'user': curuser, 'key': 'id', 'sip_auth_cnonce': 'WPywjtf8PgNdUIrezgjdg6mM-Rw-2M5x', 'sip_auth_response': '4b604606a06e9f83f5e76f9b9f66661e', 'FreeSWITCH-IPv4': self.hostip, 'sip_user_agent': 'Telephone 0.13.3', 'FreeSWITCH-IPv6': '::1', 'sip_auth_realm': self.hostip, 'sip_profile': 'test1.example.com', 'sip_auth_qop': 'auth', 'tag_name': 'domain', 'FreeSWITCH-Hostname': self.hostname, 'sip_to_user': curuser, 'action': 'sip_auth', 'Event-Calling-File': 'sofia_reg.c', 'Core-UUID': 'f46e9270-32a5-11de-bb04-791dda701640'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['xml_context'], '<result status="not found" />')
        # TODO проверка регистрация акауна
        
        # TODO акаунт отключился
        
        # print response.content
        # print " \n"
        # print " \n"
           
        #{u'domain': [u'62.149.27.151'], u'sip_contact_user': [u'2000000'], u'ip': [u'77.122.2.96'], u'sip_from_user': [u'2000000'], u'sip_auth_nc': [u'00000001'], u'section': [u'directory'], 'hostname': self.hostname, 'sip_auth_method': 'REGISTER', 'sip_auth_username': '2000000', 'sip_auth_nonce': [u'baae7dc0-1b8f-11de-8f9c-dd7bd5170c82'], u'sip_to_host': [u'62.149.27.151'], u'key_value': [u'62.149.27.151'], u'sip_request_host': [u'62.149.27.151'], u'key_name': [u'name'], u'sip_from_host': [u'62.149.27.151'], u'sip_auth_uri': [u'sip:62.149.27.151'], u'user': [u'2000000'], u'key': [u'id'], u'sip_auth_cnonce': [u'cb2e7a55be5700fc887ab6a5fe91874e'], u'sip_auth_response': [u'8cbf5090a86b00b59cab04477bcab38e'], u'sip_user_agent': [u'X-Lite release 1100l stamp 47546'], u'sip_auth_realm': [u'62.149.27.151'], u'sip_to_user': [u'2000000'], u'sip_auth_qop': [u'auth'], u'tag_name': [u'domain'], u'sip_profile': [u'internal'], u'action': [u'sip_auth'], u'sip_contact_host': [u'77.122.2.96']}
