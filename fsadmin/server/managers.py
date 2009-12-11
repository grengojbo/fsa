# -*- coding: UTF-8 -*-
from django.db import models
#from django.template import Context, loader
from django.contrib.auth.models import User
#from fsadmin.dialplan.models import Context
#from django.conf import settings
#from fsadmin.directory import Endpoint
from django.db.models import Avg, Max, Min, Count
#import logging as l

class ServerManager(models.Manager):
    """
    """
    
    def get_servers(self, name):
        """
         
        """
        return self.get(name=name, enabled=True)
    
    #def get_query_set(self):
    #    """Custom queryset"""
    #    return super(ServerManager, self).get_query_set().filter(enabled=True)
