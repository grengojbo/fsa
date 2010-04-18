# -*- mode: python; coding: utf-8; -*-
"""
config.py

Created by jbo on 2010-01-06.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
from livesettings import *
import os
import urlparse
from decimal import Decimal
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from livesettings import config_register, BooleanValue, StringValue, \
    MultipleStringValue, ConfigurationGroup, PositiveIntegerValue, \
    DecimalValue
# this is so that the translation utility will pick up the string
gettext = lambda s: s

SERVER_MODULES = config_get('SERVER', 'MODULES')
SERVER_MODULES.add_choice(('lcr', _('lcr')))

SERVER_GROUP = ConfigurationGroup('lcr', 
    _('Lcr Module Settings'), 
    requires=SERVER_MODULES,
    ordering = 100)

config_register_list(
   ModuleValue(SERVER_GROUP,
       'MODULE',
       description=_('Implementation module'),
       hidden=True,
       default = 'fsa.lcr') 
)

LCR_GROUP = ConfigurationGroup('LCR', _('Lcr Settings'), ordering=0)

config_register(PositiveIntegerValue(
    LCR_GROUP,
        'LCR_CSV',
        description = _('Default Lcr format'),
        help_text = _("CSV format file from load lcr data"),
        default = 3
    ))
