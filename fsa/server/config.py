# -*- mode: python; coding: utf-8; -*-
"""
config.py

Created by jbo on 2010-01-06.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

from django.utils.translation import ugettext_lazy, ugettext
from livesettings import *
#from satchmo_store.shop import get_satchmo_setting
from satchmo_utils import is_string_like, load_module
import logging
import signals

_ = ugettext_lazy

log = logging.getLogger('fsa.server.config')

SERVER_GROUP = ConfigurationGroup('SERVER', _('Server Settings'))

config_register_list(
    StringValue(SERVER_GROUP,
        'loglevel',
        description = _("Default Global Log Level"),
        help_text = _("Default Global Log Level - value is one of debug,info,notice,warning,err,crit,alert"),
        default='err',
        ordering=10,
        choices = (
            ('debug', _('Debug')),
            ('info', _('Info')),
            ('notice', _('Notice')),
            ('warning', _('Warning')),
            ('err', _('Error')),
            ('crit', _('Crit')),
            ('alert', _('Alert'))
        )),
    PositiveIntegerValue(SERVER_GROUP, 'log_level', default = 0,
        description = _('Log level')
    ),
    StringValue(SERVER_GROUP,
            'rcphost',
            description= _("RCP host"),
            help_text=_("Host to connect rcp"),
            default = '127.0.0.1',
            ordering=5),
    StringValue(SERVER_GROUP,
            'rcpport',
            description= _("RCP port"),
            help_text=_("port to connect rcp"),
            default = '8080',
            ordering=6),
    StringValue(SERVER_GROUP,
            'rcpuser',
            description= _("RCP User"),
            help_text=_("User to connect rcp"),
            default = 'freeswitch',
            ordering=7),
    StringValue(SERVER_GROUP,
            'rcppasswd',
            description= _("RCP Password"),
            help_text=_("Password to connect rcp"),
            default = 'works',
            ordering=8),
    PositiveIntegerValue(SERVER_GROUP, 'debug_presence', default = 0,
       description = _('Debug presence'),
               
    ),
    MultipleStringValue(SERVER_GROUP,
        'MODULES',
        description=_("Enable FreeSWITH modules"),
        help_text=_("""Select the FreeSWITH modules you want to use with your server."""),
        default=["acl", "sofia", "event_socket", "limit", "xml_cdr", "lcr"]),
    PositiveIntegerValue(
        SERVER_GROUP,
            'max_sessions',
            description = _('Most channels to allow at once'),
            default = 1000
    ),
    PositiveIntegerValue(
        SERVER_GROUP,
            'sessions_per_second',
            description = _('Most channels to create per second'),
            default = 30
    ),
    PositiveIntegerValue(
        SERVER_GROUP,
            'min_dtmf_duration',
            description = _('min dtmf duration'),
            help_text = _("The min-dtmf-duration specifies the minimum DTMF duration to use on outgoing events. Events shorter than this will be increased in duration to match min_dtmf_duration. You cannot configure a dtmf duration on a  profile that is less than this setting."),
            default = 400,
            ordering=13
    ),
    PositiveIntegerValue(
        SERVER_GROUP,
            'max_dtmf_duration',
            description = _('max dtmf duration'),
            help_text = _("The max-dtmf-duration caps the playout of a DTMF event at the specified duration. Events exceeding this duration will be truncated to this duration. You cannot configure a duration on a profile that exceeds this setting."),
            default = 192000,
            ordering=14
    ),
    PositiveIntegerValue(
        SERVER_GROUP,
            'default_dtmf_duration',
            description = _('Default dtmf duration'),
            help_text = _("The default_dtmf_duration specifies the DTMF duration to use on originated DTMF events or on events that are received without a duration specified. This value can be increased or lowered. This value is lower-bounded by min_dtmf_duration and upper-bounded by max-dtmf-duration."),
            default = 2000,
            ordering=15
    ),
    PositiveIntegerValue(
        SERVER_GROUP,
            'rtp_start_port',
            description = _('Start port'),
            help_text = _("RTP port range"),
            default = 16384
    ),
    PositiveIntegerValue(
        SERVER_GROUP,
            'rtp_end_port',
            description = _('End port'),
            help_text = _("RTP port range"),
            default = 32768
    ),
    BooleanValue(SERVER_GROUP,
        'rtp_enable_zrtp',
        description = _('Enable zrtp'),
        #help_text = _("Require a state during registration/checkout for countries that have states?"),
        default = True)
)
#_default_modules = ('acl','event_socket')
_default_modules = ('acl','cdr')
for module in _default_modules:
    try:
        load_module("fsa.%s.config" % module)
        log.debug('load: fsa.%s.config', module)
    except ImportError:
        log.debug('Could not load default module configuration: %s', module)

# --- Load any extra payment modules. ---
extra_modules = ('event_socket','limit', 'sofia', 'lcr')

for extra in extra_modules:
    try:
        load_module("fsa.server.modules.%s.config" % extra)
        log.debug('load: fsa.server.modules.%s.config', extra)
    except ImportError:
        log.warn('Could not load module configuration: %s' % extra)

# --- helper functions ---
def active_modules():
    """
    [(key), (config group),...]
    """
    #return [(module, config_get_group(module)) for module in config_value('SERVER', 'MODULES')]
    return config_value('SERVER', 'MODULES')

def credit_choices(settings=None, include_module_if_no_choices=False):
    choices = []
    keys = []
    for module in config_value('SERVER', 'MODULES'):
        vals = config_choice_values(module, 'CREDITCHOICES')
        for val in vals:
            key, label = val
            if not key in keys:
                keys.append(key)
                pair = (key, ugettext(label))
                choices.append(pair)
        if include_module_if_no_choices and not vals:
            key = config_value(module, 'KEY')
            label = config_value(module, 'LABEL')
            pair = (key, ugettext(label))
            choices.append(pair)
    return choices

def labelled_payment_choices():
    active_payment_modules = config_choice_values('SERVER', 'MODULES', translate=True)

    choices = []
    for module, module_name in active_payment_modules:
        label = _(config_value(module, 'LABEL', default = module_name))
        choices.append((module, label))
    
    signals.payment_choices.send(None, choices=choices)
    return choices
