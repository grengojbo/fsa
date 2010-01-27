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
        f = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'lcr.csv'), "rt")
        save_cnt = 0
        try:
            cd = CsvData("delimiter=';'time_format='%d.%m.%Y 00:00'name|other|pref_digits|rate")
            # delimiter=';'time_format='%d.%m.%Y 00:00'name|country_code|special_digits|rate
            reader = csv.reader(f, delimiter=';', dialect='excel')
            #l.debug
            no_base = []
            for row in reader:
                save_flag = False
                n = {}
                row_save = []
                n['country_code'] = ''
                n['special_digits'] = False
                n['date_start'] = datetime.datetime.now()
                n['date_end'] = datetime.datetime.max
                for index, c in enumerate(cd.data_col):
                    try:
                        #l.debug("%s=%s" % (c,row[index].strip()))
                        if c != 'zeros' and len(row[index].strip()) > 0:
                            if c == 'name':
                                n["name"] = row[index].strip()
                            elif c == 'rate':
                                n['rate'] = cd.set_num(row[index].strip())
                            elif c == 'country_code':
                                n['country_code'] = row[index].strip()
                            elif c == 'special_digits':
                                save_flag = True
                                n["special_digits"] = row[index].strip()
                            elif c == 'pref_digits':
                                save_flag = True
                                n["pref_digits"] = row[index].strip()
                            elif c == 'date_start' and len(row[index].strip()) > 1:
                                n['date_start'] = cd.set_time(row[index].strip())
                            elif c == 'date_end' and len(row[index].strip()) > 1:
                                n['date_end'] = cd.set_time(row[index].strip())
                            elif c == 'digits':
                                save_flag = True
                                n["digits"] = row[index].strip()
                            elif row[index].strip() != '':
                                n[c]=row[index].strip()
                    except:
                        pass
                if save_flag:
                    if n['special_digits']:
                        cd.par_spec(n['special_digits'].replace(" ", ''), n['country_code'].replace(" ", ''), n['name']) 
                    if n['pref_digits']:
                        country_list, country_code = cd.par_pref(n['pref_digits'].replace(" ", ''), n['name'])
                        for country in country_list:
                            l.debug(country)
                    elif n["digits"] != '':
                        d = '%s%s' % (n['country_code'], n["digits"])
                        #save_cnt += self.add_lcr(gw, n, d)
                        #l.debug('digits: %s/%s/' % (d,n["name"]))
                n.clear()
        except csv.Error, e:
            raise            
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
        


