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
#from fsadmin.directory.models import Endpoint, SipRegistration
from fsa.server.models import SipProfile
from fsa.gateway.models import SofiaGateway
import logging as l

class DirectoryTestCase(test.TestCase):
    # TODO добавить тесты
    fixtures = ['testsite', 'acl', 'context', 'extension', 'server', 'server_conf', 'gateway']
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

    def testGateway(self):
        """
        Tests 
        """
        lcr_format = "digits,name,rate,other,date_start,date_end"
        
        ngw = SofiaGateway.objects.create(name='test1', username='testUser', realm='realm.com', enabled=True)
        gw = SofiaGateway.objects.get(name='test1', enabled=True)
        self.assertEquals(gw.lcr_format, lcr_format)
        gt = SofiaGateway.objects.filter(enabled=True)
        self.assertEquals(gt.count(),5)
        gw.prov_url = 'http://realm.com/'
        gw.save()
        
        response = self.client.post('/gw/gw/', {'key_value': 'event_socket.conf'})
        self.assertEquals(response.status_code, 200)
        #l.debug(response.content)
        
        #gw.password = 'mypass'
        # from_user = 
        # from_domain = 
        # exten = 
        # proxy = 
        # register_proxy = 
        # expire_seconds = 
        # register = 
        # retry_seconds = 
        # register_transport = 
        # caller_id_in_from = 
        # extension_in_contact = 
        #gw.ping = ''
        # prefix = 
        # suffix = 
        # context =
        # max_concurrent =
        # in_progress_calls = 
        # direction = 
        # acl =
        
        #sofia = SipProfile.objects.get(name = 'test1.example.com', enabled=True)
        #gw = sofia.gateway.lactive()
        #self.assertEquals(gw.count(), 1)

