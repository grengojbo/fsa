# -*- mode: python; coding: utf-8; -*-
from django.db import models
#from django.template import Context, loader
from django.contrib.auth.models import User
from fsa.dialplan.models import Context
from fsa.server.models import SipProfile
#from fsa.directory.models import Endpoint as e
from django.conf import settings
#from fsa.directory.models import Endpoint, NumberPlan
from django.db.models import Avg, Max, Min, Count
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
import logging
import datetime

l = logging.getLogger('fsa.numberplan.managers')

class NumberPlanManager(models.Manager):
    def lactivate(self,pn):
        """
         Активируем номер
        pn - Phone Number 
        """
        n = self.get(phone_number=pn)
        n.enables = True
        n.status = 1
        n.date_active = datetime.datetime.now()
        n.save()
        return n

    def create_phone_number(self, phone_number, nt=0):
        new_phone = self.create(phone_number=phone_number,nt=nt, enables=True, status=1, date_active = datetime.datetime.now())
        return new_phone
    def lphonenumber(self, site=None):
        """Возвращает случайный свободный номер"""
        if site is None:
            site = Site.objects.get(pk=1)
        p = self.filter(enables=False, nt=1, status=0, site=site)[0]
        p.status = 3
        p.date_active = datetime.datetime.now()
        p.save()
        return p.phone_number

    def lfree(self,pn):
        """присваиваем статус свободный номер"""
        pass
    
    def lpark(self, pn):
        """
        Паркуем номер
        pn - Phone Number
        """
        n = self.get(phone_number=pn)
        n.enables = False
        n.status = 2
        n.date_active = datetime.datetime.now()
        n.save()
        return n

    def status_count(self):
        top = self.model.objects.values('status').annotate(score=Count('status'))
        #return [tag['status'] for tag in top]
        return top

    def type_count(self):
        """
         [{'score': 13, 'nt': 1}, {'score': 3, 'nt': 2}, {'score': 4, 'nt': 3}]
        """
        top = self.model.objects.values('nt').annotate(score=Count('nt'))
        #return [tag['nt'] for tag in top]
        return top

    def set_number(self):
        """docstring for set_number"""
        n = self.filter(enables=False, nt=1)[0]
        n.enables = True
        n.save()
        return n.phone_number

    def gen_num_plan(self, number_start, number_end, si=1):
        """
        Генерация номерного плана
        number_start 
        number_end
        """
        site = Site.objects.get(pk=si)
        for n in range(number_start, number_end+1):
            np = self.model()
            np.phone_number = str(n)
            np.site = site
            l.debug("number: %i" % n)
            np.save()
