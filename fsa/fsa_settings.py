# -*- mode: python; coding: utf-8; -*-
from settings import *

# TODO delete lib.decorators
INSTALLED_APPS += (
    'currency',
    #'fsa.core',
    'fsa.api',
    'lib',
    'bursar',
    'fsa.acl',
    'fsa.numberplan',
    'fsa.gateway',
    'fsa.server',
    'fsa.dialplan',
    'fsa.directory',
    'fsa.lcr', # lev 3
    'fsa.cdr',
    #'fsbilling.base',
    #'fsbilling.tariff',
    #'contact',
    )
