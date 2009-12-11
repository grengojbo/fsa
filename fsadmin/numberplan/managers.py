# -*- coding: UTF-8 -*-
from django.db import models
#from django.template import Context, loader
from django.contrib.auth.models import User
from fsadmin.dialplan.models import Context
from fsadmin.server.models import SipProfile
#from fsadmin.directory.models import Endpoint as e
from django.conf import settings
#from fsadmin.directory.models import Endpoint, NumberPlan
from django.db.models import Avg, Max, Min, Count
import logging
import datetime

l = logging.getLogger('fsadmin.numberplan.managers')

class NumberPlanManager(models.Manager):
    def set_number(self):
        """docstring for set_number"""
        n = self.filter(enables=False, nt=1)[0]
        n.enables = True
        n.save()
        return n.phone_number
        
    def gen_num_plan(self, number_start, number_end):
        """
        Генерация номерного плана
        number_start 
        number_end
        """
        for n in range(number_start, number_end+1):
            np = self.model()
            np.phone_number = n
            l.debug("number: %i" % n)
            np.save()
        