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
from fsa.lcr.models import Lcr
from fsa.gateway.models import SofiaGateway
import csv, sys, os
import time, datetime
from decimal import *
from fsa.core.utils import CsvData
import logging
l = logging.getLogger('fsa.lcr.tests')

class LcrTestCase(test.TestCase):
    #fixtures = ['testsite', 'alias', 'server', 'context', 'gateway', 'sipprofile', 'fsgroup', 'testendpoint', 'testcdr', 'acl']
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
    
        
    
    def testLoadCSV(self):
        """docstring for testLoadCSV"""
        try:
            #f = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_all.csv'), "rt")
            f = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'lcr_test.csv'), "rt")
            save_cnt = 0
            default_currency = 'GRN'
            curency_grn = '8.11'
            #All
            #cd = CsvData("delimiter=';'time_format='%d.%m.%Y 00:00'country_code|name|other|pref_digits|rate|currency|brand")
            # Ukraina
            #cd = CsvData("delimiter=';'time_format='%d.%m.%Y 00:00'country_code|name|digits|rate|brand|currency")
            # Russian
            cd = CsvData("delimiter=';'time_format='%d.%m.%Y 00:00'name|country_code|pref_digits|rate|currency|brand")
            # delimiter=';'time_format='%d.%m.%Y 00:00'name|country_code|special_digits|rate
            fw = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_result.csv'), "wt")
            writer = csv.writer(fw, delimiter=',', dialect='excel')
            # Abill price
            writer.writerow(('countrycode', 'pattern', 'name',	'weight', 'connectcharge', 'includedseconds', 'minimumprice', 'price', 'brand'))
            #Abill route
            #writer.writerow(('countrycode', 'routename', 'pattern', 'costplan', 'connectcharge', 'includedseconds', 'billincrement', 'minimumcost', 'cost', 'trunk'))
            reader = csv.reader(f, delimiter=';', dialect='excel')
            for row in reader:
                try:
                    #l.debug(row)
                    country_list, country_code, n = cd.parse(row)
                    l.debug(country_list)
                    for country in country_list:
                        if n['currency'] and n['currency'] != default_currency:
                            price = Decimal(n['rate']) * Decimal(curency_grn)
                        else:
                            price = Decimal(n['rate'])
                        # price
                        writer.writerow((country_code, country, n["name"],	0, Decimal('0.0000'), Decimal('0.0000'), Decimal('0.0000'), price, n['brand']))
                        # route
                        #writer.writerow((country_code, n["name"], country, 0, Decimal('0.0000'), Decimal('0.0000'), 1,   Decimal('0.0000'), price, n['brand']))
                        
                except Exception, e:
                    l.error("line: %i => %s" % (cd.line_num, e)) 
                    pass
        except Exception, e:
            l.error(e)            
        finally:
            fw.close()
            f.close()

    # def testSaveCSV(self):
    #     """docstring for testSaveCSV"""
    #     f = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'prepaid.csv'), "rt")
    #     fw = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'prepaids.csv'), "wt")
    #     try:
    #         reader = csv.reader(f, delimiter=';', dialect='excel')
    #         writer = csv.writer(fw, delimiter=';', dialect='excel')
    #         writer.writerow( ('Number', 'Code', 'Money') )
    #         m = 0
    #         for row in reader:
    #             if m < 4000:
    #                 mon = 30
    #             elif m < 7000:
    #                 mon = 50
    #             else:
    #                 mon = 80
    #             m += 1 
    #             writer.writerow( (row[0], '%s%s' % (row[1], row[2]), mon) )
    #     finally:
    #         fw.close()
    #         f.close()
            
    # def testLcrLoad(self):
    #     """docstring for testLcrLoad"""
    #     f = open(os.path.join(os.path.dirname(__file__), 'fixtures', '15.csv'), "rt")
    #     gw = SofiaGateway.objects.get(name='testgw', enabled=True)
    #     try:
    #         #reader = csv.reader(open(filename, "rb"), delimiter=';')
    #         res = Lcr.objects.load_lcr(gw, f)
    #         self.assertEquals(res, 286) 
    #     finally:
    #         f.close()
    #     f = open(os.path.join(os.path.dirname(__file__), 'fixtures', '14.csv'), "rt")
    #     gw.lcr_format = "delimiter=';'time_format='%d.%m.%Y 00:00'name|special_digits|rate"
    #     try:
    #         res = Lcr.objects.load_lcr(gw, f)
    #         self.assertEquals(res, 577) 
    #     finally:
    #         f.close()
    #     f = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test-lcr.csv'), "rt")
    #     gw.lcr_format = "delimiter=';'time_format='%d.%m.%Y 00:00'digits|name|rate|zeros|date_start|zeros"
    #     try:
    #         res = Lcr.objects.load_lcr(gw, f)
    #         self.assertEquals(res, 14) 
    #     finally:
    #         f.close()
        


