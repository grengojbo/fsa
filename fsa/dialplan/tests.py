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
from fsa.dialplan.models import Extension
import logging as l



class DialPLanTestCase(test.TestCase):
    fixtures = ['testsite', 'acl', 'alias', 'extension', 'context']
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.client = Client()

    def testDialPlan(self):
        """
        Tests 
        """
        res1 = '<extension name="dx"><condition field="destination_number" expression="^dx$"><action application="answer"/>\r\n<action application="read" data="11 11 \'tone_stream://%(10000,0,350,440)\' digits 5000 #"/>\r\n<action application="execute_extension" data="is_transfer XML features"/></condition></extension>'
        res2 = '<extension name="is_zrtp_secure" continue="true"><condition field="${zrtp_secure_media_confirmed}" expression="^true$">\r\n\t<action application="sleep" data="1000"/>\r\n\t<action application="playback" data="misc/call_secured.wav"/>\r\n\t<anti-action application="eval" data="not_secure"/>\r\n</condition></extension>'
        
        e = Extension.objects.get(pk=1)
        self.assertEquals(e.preview, res1)
        e = Extension.objects.get(pk=5)
        self.assertEquals(e.preview, res2)
        e = Extension.objects.filter(exten__name__exact='default', is_temporary=False, enabled=True)
        self.failUnlessEqual(e.count(), 0)
        ne = Extension.objects.get(pk=10)
        ne.is_temporary = False
        ne.save()
        e = Extension.objects.get_exten('default')
        self.assertEquals(e.count(), 1)
        #response = self.client.post('/cdr/set/', {'name': 'param'})
        #self.failUnlessEqual(response.status_code, 200)


