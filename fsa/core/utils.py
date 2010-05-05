# -*- mode: python; coding: utf-8; -*- 

"""
utils.py

Created by jbo on 2009-05-05.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""
import time, datetime, re, csv  
import logging
from pytils.translit import translify
from decimal import *
l = logging.getLogger('fsa.core.utils')

__author__ = '$Author$'
__revision__ = '$Revision$'

def pars_phone(phone):
    """
    from fsa.core.utils import pars_phone
    pars_phone("366667777")
    return: '366667777, 36666777, 3666677, 366667, 36666, 3666, 366, 36, 3'
    """
    res = None
    cn = len(phone)
    for r in range(0,cn):
        if res is None:
            res = phone[0:cn]
        else:
            res = "%s, %s" % (res, phone[0:cn-r])
    return res

class CsvData(object):
    """docstring for CsvFormat
    cf = "delimiter=';'time_format='%d.%m.%Y 00:00'digits|rate|date_start|zeros|date_end|other"
    dt = "22.00;22,33"
    """
    def __init__(self, cf):
        super(CsvData, self).__init__()
        rp = re.compile(r"delimiter='([,.;_\t|]{1,2})'time_format='(.*)'(.*)", re.IGNORECASE | re.DOTALL)
        (self.delimiter, self.time_format, dc ) = rp.findall(cf)[0]
        self.data_col = dc.split('|')
        self.line_num = 0
        self.line_error_list = list()
        self.line_ok = 0
        self.row = None 
        
    def set_num(self, n):
        """docstring for set_num"""
        return Decimal(n.strip().replace(',','.').replace(" ", ''))
    def set_int(self, n):
        """docstring for set_int"""
        return int(n.strip().replace(" ", ''))
    def set_boll(self, n):
        """docstring for set_int"""
        try:
            if n == '':
                return True
            res = int(n.strip().replace(" ", ''))
            if res == 1:
                return True
            return False
        except:
            return False
    def set_time(self, t):
        """docstring for set_time"""
        return datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(t + " 00:00", self.time_format)))
    
    def reader(self, f, delimiter=';', dialect='excel'):
        try:
            return csv.reader(f, delimiter=';', dialect='excel')
        finally:
            f.close()
    
    def parse(self, row):
        """docstring for parse"""
        save_flag = False
        self.row = row
        self.line_num += 1
        n = {}
        n['country_code'] = 0
        n['special_digits'] = False
        n['pref_digits'] = False
        n["digits"] = ''
        n["rate"] = ''
        n['date_start'] = datetime.datetime.now()
        n['date_end'] = datetime.datetime.max
        
        for index, c in enumerate(self.data_col):
            try:
                #l.debug("%s=%s" % (c,row[index].strip()))
                if c != 'zeros' and len(row[index].strip()) > 0:
                    if c == 'name':
                        n["name"] = row[index].strip()
                    elif c == 'rate':
                        n['rate'] = self.set_num(row[index])
                        save_flag = True
                    elif c == 'price':
                        n['price'] = self.set_num(row[index])
                        save_flag = True
                    elif c == 'country_code':
                        n['country_code'] = self.set_int(row[index])
                    elif c == 'special_digits':
                        save_flag = True
                        n["special_digits"] = row[index].strip().replace(" ", '')
                    elif c == 'pref_digits':
                        save_flag = True
                        n["pref_digits"] = row[index].strip().replace(" ", '')
                    elif c == 'date_start' and len(row[index].strip()) > 1:
                        n['date_start'] = self.set_time(row[index].strip())
                    elif c == 'date_end' and len(row[index].strip()) > 1:
                        n['date_end'] = self.set_time(row[index].strip())
                    elif c == 'time_start':
                        t = row[index].strip().replace(" ", '').split(":")
                        n['time_start'] = datetime.time(int(t[0]), int(t[1]))
                    elif c == 'time_end':
                        t = row[index].strip().replace(" ", '').split(":")
                        n['time_end'] = datetime.time(int(t[0]), int(t[1]))
                    elif c == 'digits':
                        save_flag = True
                        n["digits"] = self.set_int(row[index])
                    elif c == 'weeks':
                        n['weeks'] = row[index].strip().replace(" ", '')
                    elif row[index].strip() != '':
                        n[c]=row[index].strip()
            except Exception, e:
                #l.error(e)
                #l.error(self.row)
                self.line_error_list.append(self.row)
        if save_flag:
            if n['pref_digits']:
                country_list, country_code = self.par_pref(n['pref_digits'], n['country_code'])
                return (country_list, country_code, n)
            elif n["digits"] != '':
                country_list = list()
                #country_list.append('%s%s' % (n['country_code'], n["digits"]))
                country_list.append(int('%s' % n["digits"]))
                return (country_list, n['country_code'], n)
            elif n["rate"] != '':
                return n
                
    def par_pref(self, special_digits, name):
        """docstring for par_spec"""
        country_list = list()
        country = None
        try:
            dig_re=re.compile(r"(\d+)-(\d+)")
            delim_re = re.compile(r"[:,;]")
            d = re.compile(r"(?P<pref_country>.*)\((?P<pref_arr>.*)\)$|(?P<country>.*)$")
            #l.debug(special_digits)
            for dig in special_digits.split(';'):
                pref_digits = dig_re.match(dig)
                if pref_digits:
                    for digit in range(int(pref_digits.groups()[0]), int(pref_digits.groups()[1])+1):
                        if name != 0:
                            country = name
                            country_list.append(int('%i%i' % (name, digit)))
                        else:
                            country = digit
                            country_list.append(digit)
                else:
                    r = d.match(dig).groupdict()
                    if r.get('country'): 
                        for prefs in delim_re.split(r.get('country')):
                            pref = dig_re.match(prefs)
                            if pref:
                                for digit in range(int(pref.groups()[0]), int(pref.groups()[1])+1):
                                    #l.debug("digit: %i countrys=%s <= %s" % (digit, prefs, r.get('country')))
                                    country_list.append(digit)
                                    country = digit
                            else:
                                #l.debug("country=%s <= %s" % (prefs, r.get('country')))
                                country_list.append(int(prefs))
                                country = prefs
                    elif r.get('pref_arr') and r.get('pref_country'):
                        country = r.get('pref_country')
                        for prefs in delim_re.split(r.get('pref_arr')):
                            pref = dig_re.match(prefs)
                            if pref:
                                for digit in range(int(pref.groups()[0]), int(pref.groups()[1])+1):
                                    #l.debug("digit: %i countrys=%s <= %s" % (digit, prefs, r.get('pref_country')))
                                    country_list.append(int("%s%i" % (r.get('pref_country'), digit)))
                                    country = digit
                            else:
                                #l.debug("country=%s pref_arr=%s  (%s)" % (r.get('pref_country'), r.get('pref_arr'), prefs))
                                country_list.append(int("%s%s" % (r.get('pref_country'), prefs)))
                                country = prefs
                    else:
                        l.debug("no add: %s" % pref_digits)
            #l.debug(country_list)
            #l.debug("-------------------")
            if name != 0:
                return (country_list, name)
            elif re.compile(r"\d+").match(country):
                return (country_list, int(country))
            else:
                return (country_list, 0)
        except Exception, e:
            self.line_error_list.append(self.row)
            l.error("line:%i except: %s => %s" % (self.line_num, pref_digits, e))
        
    # def par_spec(self, special_digits, country_code, name):
    #     """docstring for par_spec"""
    #     l.debug(special_digits)
    #     for dig in special_digits.split(';'):
    #         digit = dig.split('-')
    #         if len(digit) == 2:
    #             for digits in range(int(digit[0]), int(digit[1])+1):
    #                 d = '%s%s' % (country_code.strip(), digits)
    #                 l.debug('digits: %s/%s/' % (d,name))
    #                 #save_cnt += self.add_lcr(gw, n, d)
    #         elif len(dig) > 0 and dig != '':
    #             d = '%s%s' % (country_code, dig.strip())
    #             l.debug('digits: %s/%s/%s/' % (d,name,dig))