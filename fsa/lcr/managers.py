# -*- mode: python; coding: utf-8; -*- 

from django.db import models
from django.db import connection
import logging, re, string, csv
import time, datetime
from fsa.core.utils import CsvData
#from django.template import Context, loader
from django.contrib.auth.models import User
#from fsa.dialplan.models import Context
#from django.conf import settings
#from fsa.directory import Endpoint
from django.utils.encoding import force_unicode
from django.db.models import F, Q
from django.db.models import Max, Min, Avg, Sum, Count, StdDev, Variance
from currency.money import Money
from currency.models import Currency
l = logging.getLogger('fsa.lcr.managers')

class LcrManager(models.Manager):
    """
    """
    def add_lcr(self, gw, n, digits, price, site):
        lc = self.model()
        lc.name = n['name']
        # TODO проверка на неправильный формат, замена 5,12->5.12
        lc.rate = n['rate']
        lc.date_start = n['date_start']
        lc.date_end = n['date_end']
        if n['time_start']:
            t = n['time_start'].split(":")
            lc.time_start = datetime.time(int(t[0]), int(t[1]))
        if n['time_end']:
            t = n['time_end'].split(":")
            lc.time_start = datetime.time(int(t[0]), int(t[1]))
        lc.lead_strip = 0
        if n['week1']:
            lc.week1 = n['week1']
        if n['week2']:
            lc.week2 = n['week2']
        if n['week3']:
            lc.week3 = n['week3']
        if n['week4']:
            lc.week4 = n['week4']
        if n['week5']:
            lc.week5 = n['week5']
        if n['week6']:
            lc.week6 = n['week6']
        if n['week7']:
            lc.week7 = n['week7']
        lc.trail_strip = 0
        lc.quality = 0
        lc.reliability = 0
        lc.enabled = True
        lc.carrier_id = gw
        lc.digits = digits
        lc.price = price
        lc.site = site
        lc.save()
        return 1
        
    def load_lcr(self, gw, base_file):
        """
        Загрузка данных из csv файла
        для успешной lcr загрузки необходимо в таблице gateway конфигурации
        прописать lcr_format 
        """
        save_cnt = 0
        try:
            cd = CsvData(gw.lcr_format)
            reader = csv.reader(base_file, delimiter=';', dialect='excel')
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
                        l.debug(n['special_digits'])
                        for dig in n['special_digits'].split(';'):
                            digit = dig.split('-')
                            if len(digit) == 2:
                                for digits in range(int(digit[0]), int(digit[1])+1):
                                    d = '%s%s' % (n['country_code'].strip(), digits)
                                    l.debug('digits: %s/%s/' % (d,n["name"]))
                                    save_cnt += self.add_lcr(gw, n, d)
                            elif len(dig) > 0 and dig != '':
                                d = '%s%s' % (n['country_code'], dig.strip())
                                l.debug('digits: %s/%s/%s/' % (d,n["name"],dig))
                                save_cnt += self.add_lcr(gw, n, d)
                    elif n["digits"] != '':
                        d = '%s%s' % (n['country_code'], n["digits"])
                        save_cnt += self.add_lcr(gw, n, d)
                        l.debug('digits: %s/%s/' % (d,n["name"]))
                n.clear()
        except csv.Error, e:
            l.error('line %d: %s' % (reader.line_num, e))
        #self.cnt += save_cnt
        #self.save()
        #if len(no_base) > 0:
        #    return no_base
        return save_cnt
