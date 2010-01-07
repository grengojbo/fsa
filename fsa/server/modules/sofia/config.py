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
SERVER_MODULES.add_choice(('sofia', _('SIP Profiles')))

SERVER_GROUP = ConfigurationGroup('sofia', 
    _('SIP Profiles allow you to define paths to devices or carriers that may live inside or outside your network.'), 
    requires=SERVER_MODULES,
    ordering = 101)

config_register_list(
   ModuleValue(SERVER_GROUP,
       'MODULE',
       description=_('Implementation module'),
       hidden=True,
       default = 'fsa.server.modules.sofia')
)
# <!-- <param name="auto-restart" value="false"/> -->
