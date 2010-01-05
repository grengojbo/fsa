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
from fsa.server.models import Server, SipProfile, Conf
from fsa.dialplan.models import Context
from fsa.server import views as sv
from fsa.acl.models import FSAcl

class ServerTestCase(test.TestCase):
    # TODO проблемы при загрузке таблицы alias почемуто несоздается колонка alias_type
    fixtures = ['testsite', 'acl', 'alias', 'extension', 'context', 'server', 'server_conf']
    #fixtures = ['testsite', 'acl', 'alias', 'context', 'server', 'server.conf', 'gateway', 'sipprofile', 'fsgroup', 'testendpoint', 'testcdr']
    
    def setUp(self):
        #cont1 = Context(name="default", default_context=True)
        #cont1.save()
        #cont2 = Context(name="public", default_context=False)
        #cont2.save()
        #cont3 = Context(name="private", default_context=False)
        #cont3.save()
        #self.user = User.objects.create_user('test', 'test@test.com', 'test')
        # Every test needs a client.
        #self.client = Client()
        #self.uid = 3000
        #self.p = "123456"
        #self.effective_caller_id_name = self.uid
        #self.enable = True
        self.serv_name = 'test1.example.com'

    def testAcl(self):
        nls = FSAcl.objects.filter(server_acl__name__exact=self.serv_name,enabled=True)
        self.assertEquals(nls.count(), 2)
                
    def testConf(self):
        key_value = 'local_stream.conf'
        ls = Conf.objects.get(server__name__exact=self.serv_name, enabled=True, name__exact=key_value)
        self.assertEquals(ls.name, 'local_stream.conf')
        try:
            ls = Conf.objects.get(server__name__exact=self.serv_name, enabled=True, name__exact='no_key_value')
            xml_context = None
        except ls.DoesNotExist:
            xml_context = '<result status="not found" />'
            ls = None
        self.assertEquals(xml_context, '<result status="not found" />')
        self.assertEquals(ls, None)    
        
        
    def testGetServer(self):
        """
        Tests 
        """
        #res = Endpoint.objects.get_next_number()
        #self.assertEquals(res, 2000005)
        #c = Context.objects.filter(name='private')
        #self.failUnlessEqual(res, 2000)
        #response = self.client.post('/cdr/set/', {'name': 'param'})
        
        s = Server.objects.get_servers(self.serv_name)
        self.assertEquals(s.name, self.serv_name)
        ##ss = SipProfile.objects.filter(enabled=True)
        ##self.assertEquals(ss.count(), 1)
        
        # TODO: сервер неактивен
        #s1 = Server.objects.get_servers('test2.example.com')
        #self.assertEquals(s1, True)
        #self.failUnlessEqual(response.status_code, 200)Server.objects.get(name='linktel.com.ua')

    def testWebGetServer(self):
        """
        Добавляем sip для пользователя
        """
        #new_endpoint = Endpoint.objects.create_endpoint(self.user)
        #self.assertEquals(new_endpoint.accountcode.pk, 1)
        #self.assertEquals(self.user.username, 'test')
        #self.assertEquals(self.user.is_active, True)
        pass


