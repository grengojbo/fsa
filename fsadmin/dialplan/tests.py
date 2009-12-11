# -*- coding: UTF-8 -*-
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

__author__ = '$Author:$'
__revision__ = '$Revision:$'

import unittest
from django.test.client import Client
#from django.test import TestCase

class NameTestCase(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        #self.client = Client()
		pass

    def test_name(self):
        """
        Tests 
        """
        self.failUnlessEqual(1 + 1, 2)
        #response = self.client.post('/cdr/set/', {'name': 'param'})
        #self.failUnlessEqual(response.status_code, 200)


