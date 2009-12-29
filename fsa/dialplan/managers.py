# -*- mode: python; coding: utf-8; -*-
from django.db import models
from django.db.models import Avg, Max, Min, Count
import logging as l

class DialPLanManager(models.Manager):
    """
    """
    
    def lactive(self):
        return self.filter(is_temporary=False, enabled=True)
        
    def get_exten(self, name):
        return self.filter(exten__name__exact=name, is_temporary=False, enabled=True)