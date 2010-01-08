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
#from fsa.directory.models import Endpoint, SipRegistration
from fsa.acl.models import FSAcl, AclNetworkList
#from django.test import TestCase

class AclTestCase(test.TestCase):
    fixtures = ['testsite', 'acl']
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.client = Client()

    def testAcl(self):
        """
        Tests 
        """
        f = FSAcl.objects.filter(acls__pk=2, enabled=True)
        self.assertEquals(f.count(), 2)
        self.assertEquals(f[0].nodes.count(), 2)
        self.assertEquals(f[1].nodes.count(), 1)
        

