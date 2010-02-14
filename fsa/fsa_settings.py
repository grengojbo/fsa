# -*- mode: python; coding: utf-8; -*-
from settings import *

# TODO delete lib.decorators
INSTALLED_APPS += (
    'fsa.core',
    'fsa.api',
    'lib',
    'fsa.acl',
    'fsa.numberplan',
    'fsa.gateway',
    'fsa.server',
    'fsa.dialplan',
    'fsa.directory',
    'fsa.lcr',
    'fsa.cdr',
    #'fsbilling.base',
    #'fsbilling.tariff',
    #'contact',
    )
