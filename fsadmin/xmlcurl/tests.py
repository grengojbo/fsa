# -*- mode: python; coding: utf-8; -*-
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
#from fsa.directory.models import Endpoint, SipRegistration
#from fsa.dialplan.models import Context
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
        response1 = self.client.post('/xmlcurl/get/', {'key_value': 'xml_cdr.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response1.status_code, 200)
        
        # TODO: is not hostname
        #

        #l.debug("sofia.conf >>> %s " % response2.context['ss'])
        #self.assertEquals(response2.context['sofia.server.sql_name'], 'fsmysql') 
        
        #response = self.client.post('/xmlcurl/get/', {'key_value': 'conference.conf', 'presence': 'true', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        #self.failUnlessEqual(response.status_code, 200)
        #response = self.client.post('/xmlcurl/get/', {'key_value': 'fifo.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        #self.failUnlessEqual(response.status_code, 200)
        #response = self.client.post('/xmlcurl/get/', {'key_value': 'voicemail.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        #self.failUnlessEqual(response.status_code, 200)
        
        response = self.client.post('/xmlcurl/get/', {'key_value': 'local_stream.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['xml_context'], self.xml_context)
        
        ##{'key_value': 'spidermonkey.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': 'grengo.colocall.net', 'tag_name': 'configuration'}
        ##{'key_value': 'lua.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': 'grengo.colocall.net', 'tag_name': 'configuration'}
        ##{'key_value': 'post_load_modules.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': 'grengo.colocall.net', 'tag_name': 'configuration'}
        
        response = self.client.post('/xmlcurl/get/', {'key_value': 'acl.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response.status_code, 200)
        
        #response = self.client.post('/xmlcurl/get/', {'key_value': 'lcr.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        #self.assertEquals(response.status_code, 200)
        
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
        
        response = self.client.post('/api/get/', {'profile': 'test1.example.com', 'key_value': '', 'key_name': '', 'section': 'directory', 'hostname': self.hostname, 'tag_name': '', 'purpose': 'gateways'})
        self.assertEquals(response.status_code, 200)
        ##         data: [hostname=sip&section=directory&tag_name=domain&key_name=name&key_value=195.5.22.146&key=id&user=1000&domain=195.5.22.146]

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
##         mod_xml_curl.c:304 Received HTTP error 500 trying to fetch ##2010-05-02 23:24:16.495989 [ERR] mod_xml_curl.c:304 Received HTTP error 500 trying to fetch http://192.168.122.105:8001/api/get/
##data: [hostname=sip&section=directory&tag_name=domain&key_name=name&key_value=195.5.22.146&Event-Name=REQUEST_PARAMS&Core-UUID=fc6796e2-5627-11df-91a6-61df35aaf424&FreeSWITCH-Hostname=sip&FreeSWITCH-IPv4=195.5.22.146&FreeSWITCH-IPv6=2001%3A470%3A1f0a%3A1017%3A%3A2&Event-Date-Local=2010-05-02%2023%3A24%3A16&Event-Date-GMT=Sun,%2002%20May%202010%2020%3A24%3A16%20GMT&Event-Date-Timestamp=1272831856424667&Event-Calling-File=sofia_reg.c&Event-Calling-Function=sofia_reg_parse_auth&Event-Calling-Line-Number=1797&action=sip_auth&sip_profile=internal&sip_user_agent=Telephone%200.14.3&sip_auth_username=1000&sip_auth_realm=195.5.22.146&sip_auth_nonce=adf68b70-5628-11df-91bd-61df35aaf424&sip_auth_uri=sip%3A5000%40195.5.22.146&sip_contact_user=1000&sip_contact_host=193.201.83.3&sip_to_user=5000&sip_to_host=195.5.22.146&sip_from_user=1000&sip_from_host=195.5.22.146&sip_request_user=5000&sip_request_host=195.5.22.146&sip_auth_qop=auth&sip_auth_cnonce=9Y8mfgtWkVdwywLEJVzUKaF-SpwtlW6G&sip_auth_nc=00000001&sip_auth_response=4fdb444020ee6b66483cc44b7cc01f25&sip_auth_method=INVITE&key=id&user=1000&domain=195.5.22.146&ip=193.201.83.3]
##data: [hostname=sip&section=directory&tag_name=domain&key_name=name&key_value=195.5.22.146&Event-Name=REQUEST_PARAMS&Core-UUID=fc6796e2-5627-11df-91a6-61df35aaf424&FreeSWITCH-Hostname=sip&FreeSWITCH-IPv4=195.5.22.146&FreeSWITCH-IPv6=2001%3A470%3A1f0a%3A1017%3A%3A2&Event-Date-Local=2010-05-02%2023%3A25%3A41&Event-Date-GMT=Sun,%2002%20May%202010%2020%3A25%3A41%20GMT&Event-Date-Timestamp=1272831941255123&Event-Calling-File=sofia_reg.c&Event-Calling-Function=sofia_reg_parse_auth&Event-Calling-Line-Number=1797&action=sip_auth&sip_profile=internal&sip_user_agent=Telephone%200.14.3&sip_auth_username=1000&sip_auth_realm=195.5.22.146&sip_auth_nonce=e05e1740-5628-11df-91c1-61df35aaf424&sip_auth_uri=sip%3A195.5.22.146&sip_contact_user=1000&sip_contact_host=193.201.83.3&sip_to_user=1000&sip_to_host=195.5.22.146&sip_from_user=1000&sip_from_host=195.5.22.146&sip_request_host=195.5.22.146&sip_auth_qop=auth&sip_auth_cnonce=wnMt9DVNxoGC6H1OP-VrG3hWSOkhyoVH&sip_auth_nc=00000001&sip_auth_response=fa6b8ed25615760debec41617b8cda48&sip_auth_method=REGISTER&key=id&user=1000&domain=195.5.22.146&ip=193.201.83.3]
         #Received HTTP error 500 trying to fetch http://192.168.122.105:8001/api/get/
         #data: [hostname=sip&section=directory&tag_name=&key_name=&key_value=&Event-Name=REQUEST_PARAMS&Core-UUID=89bbe170-5627-11df-a956-3d430f7d0fc2&FreeSWITCH-Hostname=sip&FreeSWITCH-IPv4=195.5.22.146&FreeSWITCH-IPv6=2001%3A470%3A1f0a%3A1017%3A%3A2&Event-Date-Local=2010-05-02%2023%3A16%3A09&Event-Date-GMT=Sun,%2002%20May%202010%2020%3A16%3A09%20GMT&Event-Date-Timestamp=1272831369113805&Event-Calling-File=sofia.c&Event-Calling-Function=config_sofia&Event-Calling-Line-Number=3486&purpose=gateways&profile=internal