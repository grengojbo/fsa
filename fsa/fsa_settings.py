# -*- mode: python; coding: utf-8; -*-
from settings import *

# TODO delete lib.decorators
INSTALLED_APPS += (
    'fsa.core',
    'fsa.api',
    'lib',
    'bursar',
    'currency', # lev 2
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
