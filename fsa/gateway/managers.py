# -*- mode: python; coding: utf-8; -*-
from django.db import models
#from django.template import Context, loader
#from django.contrib.auth.models import User
#from fsa.gateway.models import SofiaGateway
#from fsa.directory.models import Endpoint as e
#from django.conf import settings
#from fsa.directory import Endpoint
#from django.db.models import Avg, Max, Min, Count
#import logging as l
#import datetime

class GatewayManager(models.Manager):
    """
    """
    def lactive(self):
        """
        return -- только активные шлюзы
        """
        return self.filter(enabled=True)
    

