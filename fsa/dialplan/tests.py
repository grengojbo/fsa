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
from fsa.dialplan.models import SipProfile
import logging as l

class DialPLanTestCase(test.TestCase):
    fixtures = ['testsite', 'acl', 'extension', 'context']
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.client = Client()

    def testDialPlan(self):
        """
        Tests 
        """
        pass
        #self.failUnlessEqual(1 + 1, 2)
        
            #response = self.client.post('/cdr/set/', {'name': 'param'})
        #self.failUnlessEqual(response.status_code, 200)


