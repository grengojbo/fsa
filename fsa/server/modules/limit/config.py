# -*- mode: python; coding: utf-8; -*-
"""
config.py

Created by jbo on 2010-01-06.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
from livesettings import *
from django.utils.translation import ugettext_lazy as _

# this is so that the translation utility will pick up the string
gettext = lambda s: s

SERVER_MODULES = config_get('SERVER', 'MODULES')
SERVER_MODULES.add_choice(('limit', _('limit')))

SERVER_GROUP = ConfigurationGroup('limit', 
    _('Resource limitation'), 
    requires=SERVER_MODULES,
    ordering = 102)

config_register_list(
   ModuleValue(SERVER_GROUP,
       'MODULE',
       description=_('Implementation module'),
       hidden=True,
       default = 'fsa.server.modules.limit') 
)