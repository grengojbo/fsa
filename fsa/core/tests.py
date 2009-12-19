# -*- coding: UTF-8 -*-
from django import test
from django.core import mail
from django.test.client import Client
from django.contrib.auth.models import User

#from lib.helpers import reverse
from fsa.core import appcheck    
from fsa.core import is_app
import logging as l

class CoreTestCase(test.TestCase):
    #fixtures = ['context', 'extension', 'alias', 'server', 'acl', 'gateway', 'fsgroup', 'sipprofile', 'testnp', 'testenpoint']
    #fixtures = ['testsite', 'alias', 'context', 'extension', 'server', 'acl', 'gateway', 'fsgroup', 'sipprofile', 'testnp', 'testendpoint', 'testcdr']
    fixtures = ['testsite', 'acl', 'context', 'extension', 'server', 'server_conf']
    def setUp(self):
        # Every test needs a client.
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.hostname = 'test1.example.com'
        self.hostip = '192.168.51.100'
        self.domainname = '192.168.51.100'
        self.xml_context = '<result status="not found" />'
        self.client = Client()

    def testAppcheck(self):
        tr = 0
        if is_app('fsa.core'):
            tr = 1
        self.assertEqual(tr, 1)
        tr = 0
        if is_app('fsadmin.nax'):
            tr = 1
        self.assertEqual(tr, 0)
    
    def testApiConfiguration(self):
        """
        Test Configuration section
        """
        response = self.client.post('/api/get/', {'key_value': 'event_socket.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response.status_code, 200)
        #l.debug(response)
        
        response = self.client.post('/api/get/', {'key_value': 'acl.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response.status_code, 200)
        #l.debug(response)
        
        response = self.client.post('/api/get/', {'key_value': 'local_stream.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response.status_code, 200)
        response = self.client.post('/api/get/', {'key_value': 'switch.conf', 'key_name': 'name', 'section': 'configuration', 'hostname': self.hostname, 'tag_name': 'configuration'})
        self.assertEquals(response.status_code, 200)
        
        #l.debug(response)
        #self.assertEquals(response.context['xml_context'], self.xml_context)
    


