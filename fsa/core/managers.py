# -*- mode: python; coding: utf-8; -*-
"""
http://webnewage.org/2009/1/23/kak-pravilno-otdavat-komandyi/
"""
from django.db import models
#import logging
#l = logging.getLogger('fsa.core.managers')

class GenericManager( models.Manager ):
    """
    Filters query set with given selectors 
    
    Example
    from fsa.core.managers import GenericManager
    
    class Entry( models.Model ):
        #...
        active = models.BooleanField( default = True )

        #managers
        objects = models.Manager() # default manager must be always on first place! It's used as default_manager
        active_objects = GenericManager( active = True ) # only active entries
        inactive_objects = GenericManager( active = False ) # only inactive entries
    
    """
    def __init__(self, **kwargs):
        super( GenericManager, self ).__init__()
        self.selectors = kwargs

    def get_query_set(self):
        return super( GenericManager, self ).get_query_set().filter( **self.selectors )