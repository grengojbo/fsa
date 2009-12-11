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
