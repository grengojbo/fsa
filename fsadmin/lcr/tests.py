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
from fsadmin.lcr.models import Lcr
from fsa.gateway.models import SofiaGateway
import csv, sys, os

class LcrTestCase(test.TestCase):
    fixtures = ['testsite', 'alias', 'server', 'context', 'gateway', 'sipprofile', 'fsgroup', 'testendpoint', 'testcdr', 'acl']
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        
    def testLcrLoad(self):
        """docstring for testLcrLoad"""
        f = open(os.path.join(os.path.dirname(__file__), 'fixtures', '15.csv'), "rt")
        gw = SofiaGateway.objects.get(name='testgw', enabled=True)
        try:
            #reader = csv.reader(open(filename, "rb"), delimiter=';')
            res = Lcr.objects.load_lcr(gw, f)
            self.assertEquals(res, 286) 
        finally:
            f.close()
        f = open(os.path.join(os.path.dirname(__file__), 'fixtures', '14.csv'), "rt")
        gw.lcr_format = "delimiter=';'time_format='%d.%m.%Y 00:00'name|special_digits|rate"
        try:
            res = Lcr.objects.load_lcr(gw, f)
            self.assertEquals(res, 577) 
        finally:
            f.close()
        f = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test-lcr.csv'), "rt")
        gw.lcr_format = "delimiter=';'time_format='%d.%m.%Y 00:00'digits|name|rate|zeros|date_start|zeros"
        try:
            res = Lcr.objects.load_lcr(gw, f)
            self.assertEquals(res, 14) 
        finally:
            f.close()
        


