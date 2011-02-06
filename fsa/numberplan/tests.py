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
from fsa.numberplan.models import NumberPlan
from fsa.dialplan.models import Context
#from django.test import TestCase

class NumberPLanTestCase(test.TestCase):
    fixtures = ['testsite', 'testnp']
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
        self.serv_name = 'test1.example.com'

    def testNumberPLan(self):
        r = NumberPlan.objects.lphonenumber()
        self.assertEquals(r, '1003')
        n = NumberPlan.objects.lactivate(r)
        r = NumberPlan.objects.lphonenumber()
        self.assertEquals(r, '1004')
        r = NumberPlan.objects.lphonenumber()
        self.assertEquals(r, '1006')
        
    def testNextNnumber(self):
        """
        Tests 
        """
        n = NumberPlan.objects.gen_num_plan(2011, 2020)
        res = NumberPlan.objects.all()
        self.assertEquals(res.count(), 31)
        res = NumberPlan.objects.filter(enables=False, nt=1)
        #res = Endpoint.objects.get_next_number()
        self.assertEquals(res.count(), 26)
        # res1 = NumberPlan.objects.set_number()
        # self.assertEquals(res1, 2001)
        #c = Context.objects.filter(name='private')
        #self.failUnlessEqual(res, 2000)
        #response = self.client.post('/cdr/set/', {'name': 'param'})
        #self.failUnlessEqual(response.status_code, 200)
        n = NumberPlan.objects.create_phone_number('4040', 0)
        self.assertEquals(n.enables, True)