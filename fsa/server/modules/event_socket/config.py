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
SERVER_MODULES.add_choice(('event_socket', _('event socket')))

SERVER_GROUP = ConfigurationGroup('event_socket', 
    _('Is a TCP based interface to control FreeSWITCH'), 
    requires=SERVER_MODULES,
    ordering = 103)

config_register_list(
   ModuleValue(SERVER_GROUP,
       'MODULE',
       description=_('Implementation module'),
       hidden=True,
       default = 'fsa.server.modules.event_socket') 
)