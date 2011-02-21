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
from decimal import Decimal
from decimal import *
from fsa.core.utils import CsvData
from livesettings import ConfigurationSettings, config_value, config_choice_values
from BeautifulSoup import BeautifulStoneSoup as Soup

import logging
l = logging.getLogger('fsa.lcr.tests')

class LcrTestCase(test.TestCase):
    #fixtures = ['testsite', 'alias', 'server', 'context', 'gateway', 'sipprofile', 'fsgroup', 'testendpoint', 'testcdr', 'acl']
    fixtures = ['testsite', 'currency_default', 'test_currency', 'acl', 'alias', 'extension', 'context', 'server', 'server_conf', 'gateway', 'sipprofile']
    def setUp(self):
        # Every test needs a client.
        self.client = Client()



    def testLoadCSV(self):
        """docstring for testLoadCSV"""
        try:
            from fsa.lcr.models import Lcr
            from fsa.gateway.models import SofiaGateway
            #from currency.money import Money
            #from currency.models import Currency
            from django.contrib.sites.models import RequestSite
            from django.contrib.sites.models import Site
            #f = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_all.csv'), "rt")
            f = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'lcr_test.csv'), "rt")
            gw = 3
            site = 1
            gateway = SofiaGateway.objects.get(pk=gw, enabled=True)
            s = Site.objects.get(pk=site)
            save_cnt = 0
            #default_currency = 'GRN'
            #curency_grn = '8.11'
            #All
            #cd = CsvData("delimiter=';'time_format='%d.%m.%Y 00:00'country_code|name|other|pref_digits|rate|currency|brand")
            # Ukraina
            #cd = CsvData("delimiter=';'time_format='%d.%m.%Y 00:00'country_code|name|digits|rate|brand|currency")
            # Russian
            cd = CsvData("delimiter=';'time_format='%d.%m.%Y 00:00'country_code|name|digits|price|rate|currency|weeks|time_start|time_end")
            # delimiter=';'time_format='%d.%m.%Y 00:00'name|country_code|special_digits|rate
            #fw = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_result.csv'), "wt")
            #writer = csv.writer(fw, delimiter=',', dialect='excel')
            # Abill price
            #writer.writerow(('countrycode', 'pattern', 'name',	'weight', 'connectcharge', 'includedseconds', 'minimumprice', 'price', 'brand'))
            #Abill route
            #writer.writerow(('countrycode', 'routename', 'pattern', 'costplan', 'connectcharge', 'includedseconds', 'billincrement', 'minimumcost', 'cost', 'trunk'))
            reader = csv.reader(f, delimiter=';', dialect='excel')
            for row in reader:
                try:
                    #l.debug(row)
                    country_list, country_code, n = cd.parse(row)
                    l.debug(country_code)
                    for country in country_list:
                        n['country_code'] = country_code
                        digits = n['digits']
                        #price = Money(n['price'], n['currency'])
                        price = Money(n['price'], 'USD')
                        #price = n['price']
                        objects_in_fixture = Lcr.objects.add_lcr(gateway, n, digits, price, s)
                        save_cnt += objects_in_fixture
                        #l.debug(price)
                        #l.debug(n["time_start"])
                        #, n["name"], price )
                        # route
                        #writer.writerow((country_code, n["name"], country, 0, Decimal('0.0000'), Decimal('0.0000'), 1,   Decimal('0.0000'), price, n['brand']))

                except Exception, e:
                    l.error("line: %i => %s" % (cd.line_num, e))
                    pass
            self.assertEquals(save_cnt, 3)
            res = Lcr.objects.get(digits="38039")
            self.assertEquals(res.country_code, 380)
            self.assertEquals(res.time_start, datetime.time(0, 10))
            self.assertEquals(res.time_end, datetime.time(23, 54))
            self.assertEquals(res.rate, Decimal("0.804"))
            self.assertEquals(res.price, Decimal("0.67"))
            cur = Currency.objects.get_default()
            self.assertEquals(cur.currency.iso3_code, "USD")
            exc = Currency.objects.get_currency("EUR")
            self.assertEquals(exc.exchange_rate, Decimal("1.39"))

        except Exception, e:
            l.error(e)
        finally:
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

    def testLcrLoad(self):
        """docstring for testLcrLoad"""
        resp = '<result>\n  <row id="1">    <prefix>380</prefix>    <carrier_name>ukrtelecom</carrier_name>    <rate>0.22800</rate>    <codec></codec>    <cid></cid>    <dialstring>[lcr_carrier=ukrtelecom,lcr_rate=0.22800]sofia/external/380443615162</dialstring>  </row></result>'
        self.assertEquals(config_value('SERVER', 'rcphost'), '127.0.0.1')
        self.assertEquals(config_value('SERVER', 'rcpport'), '8080')
        self.assertEquals(config_value('SERVER', 'rcpuser'), 'freeswitch')
        self.assertEquals(config_value('SERVER', 'rcppasswd'), 'works')
        xml_resp = Soup(resp)
        self.assertEquals(xml_resp.row.rate.string, '0.22800')
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



