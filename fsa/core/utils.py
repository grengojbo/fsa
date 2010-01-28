# -*- mode: python; coding: utf-8; -*- 

"""
utils.py

Created by jbo on 2009-05-05.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""
import time, datetime, re, csv  
import logging
from pytils.translit import translify

l = logging.getLogger('fsa.core.utils')

__author__ = '$Author$'
__revision__ = '$Revision$'

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
        
    def set_num(self, n):
        """docstring for set_num"""
        return n.replace(',','.')
                
    def set_time(self, t):
        """docstring for set_time"""
        return datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(t + " 00:00", self.time_format)))    
    
    def par_pref(self, pref_digits, name):
        """docstring for par_spec"""
        country_list = list()
        country = None
        try:
            delim_re = re.compile(r"[:,;]")
            d = re.compile(r"(?P<pref_country>.*)\((?P<pref_arr>.*)\)$|(?P<country>.*)$")
            r = d.match(pref_digits).groupdict()
            if r.get('country'):
                #l.debug("country=%s (%s)" % (r.get('country'), pref_digits)) 
                country_list.extend(delim_re.split(r.get('country')))
                country = r.get('country')
            elif r.get('pref_arr') and r.get('pref_country'):
                #country_list.extend(delim_re.split(r.get('pref_country')))
                country = r.get('pref_country')
                #l.debug("country=%s pref_arr=%s  (%s)" % (r.get('pref_country'), r.get('pref_arr'), pref_digits))
                for pref in delim_re.split(r.get('pref_arr')):
                    country_list.append("%s%s" % (r.get('pref_country'), pref))
                    
            else:
                l.debug("no add: %s" % pref_digits)
                
        except:
            l.debug("except: (%s)" % pref_digits)
            #continue
        l.debug(country_list)
        try:
            if re.compile(r"\d+").match(country):
                return (country_list, int(country))
            else:
                return (country_list, 0)
        except Exception, e:
            return (country_list, 0)
        
    def par_spec(self, special_digits, country_code, name):
        """docstring for par_spec"""
        l.debug(special_digits)
        for dig in special_digits.split(';'):
            digit = dig.split('-')
            if len(digit) == 2:
                for digits in range(int(digit[0]), int(digit[1])+1):
                    d = '%s%s' % (country_code.strip(), digits)
                    l.debug('digits: %s/%s/' % (d,name))
                    #save_cnt += self.add_lcr(gw, n, d)
            elif len(dig) > 0 and dig != '':
                d = '%s%s' % (country_code, dig.strip())
                l.debug('digits: %s/%s/%s/' % (d,name,dig))