# -*- mode: python; coding: utf-8; -*- 
"""
config.py

Created by jbo on 2010-01-08.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
from livesettings import *
from django.utils.translation import ugettext_lazy as _

# this is so that the translation utility will pick up the string
gettext = lambda s: s

ENDPOINT_GROUP = ConfigurationGroup('directory', _('Endpoint Module Settings'))

ENDPOINT_PREFIX = config_register(StringValue(ENDPOINT_GROUP, 'epref', default='38089', 
    description=_("Endpoint Prefix"), help_text=_(u"prefix 38089 + endpoint number 5554433 = calleredID 380895554433") 
))
config_register(BooleanValue(ENDPOINT_GROUP,
        'AUTO_CREATE',
        description= _("Auto create endpoint"),
        help_text=_("with the registration of user automatically it is created."),
        default=False, 
        ordering=5))

# --- Load any extra tax modules. ---
# extra_tax = get_satchmo_setting('CUSTOM_TAX_MODULES')
# for extra in extra_tax:
#     try:
#         load_module("%s.config" % extra)
#     except ImportError:
#         log.warn('Could not load tax module configuration: %s' % extra)

