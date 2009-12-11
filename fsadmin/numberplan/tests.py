# -*- coding: UTF-8 -*-
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
from fsadmin.numberplan.models import NumberPlan
from fsadmin.dialplan.models import Context
#from django.test import TestCase

class DirectoryTestCase(test.TestCase):
    fixtures = ['context', 'extension', 'alias', 'server', 'acl', 'gateway', 'fsgroup', 'sipprofile', 'testnp', 'testenpoint']
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

    def testNextNnumber(self):
        """
        Tests 
        """
        n = NumberPlan.objects.gen_num_plan(2011, 2020)
        res = NumberPlan.objects.filter(enables=False, nt=1)
        #res = Endpoint.objects.get_next_number()
        self.assertEquals(res.count(), 20)
        res1 = NumberPlan.objects.set_number()
        self.assertEquals(res1, 2001)
        #c = Context.objects.filter(name='private')
        #self.failUnlessEqual(res, 2000)
        #response = self.client.post('/cdr/set/', {'name': 'param'})
        #self.failUnlessEqual(response.status_code, 200)
