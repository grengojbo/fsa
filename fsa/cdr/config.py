# -*- mode: python; coding: utf-8; -*-
"""
config.py

Created by jbo on 2010-01-07.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
from livesettings import *
from django.utils.translation import ugettext_lazy as _

# this is so that the translation utility will pick up the string
gettext = lambda s: s

SERVER_MODULES = config_get('SERVER', 'MODULES')
SERVER_MODULES.add_choice(('xml_cdr', _('CDR XML')))

SERVER_GROUP = ConfigurationGroup('xml_cdr', 
    _('CDR XML Module Settings'), 
    requires=SERVER_MODULES,
    ordering = 104)

config_register_list(
    StringValue(SERVER_GROUP, 'url', default='http://localhost/api/cdr/', 
        description=_("URL"), help_text=_(u"the url to post to if blank web posting is disabled") 
    ),
    StringValue(SERVER_GROUP, 'user', default='freeswitch', 
        description=_("User"), help_text=_(u"optional: credentials to send to web server") 
    ),
    StringValue(SERVER_GROUP, 'passwd', default='freeswitch', 
        description=_("Password"), help_text=_(u"optional: credentials to send to web server") 
    ),
    IntegerValue(SERVER_GROUP, 'retries', default=2, 
        description=_("Retries"), help_text=_(u"the total number of retries (not counting the first try) to post to webserver incase of failure") 
    ),
    IntegerValue(SERVER_GROUP, 'delay', default=1, 
        description=_("Delay"), help_text=_(u"delay between retries in seconds, default is 5 seconds") 
    ),
    StringValue(SERVER_GROUP, 'log_dir', default='', 
        description=_("Log DIR"), help_text=_(u"optional: if not present we do not log every record to disk either an absolute path, a relative path assuming ${prefix}/logs or a blank value will default to ${prefix}/logs/xml_cdr") 
    ),
    BooleanValue(SERVER_GROUP, 'log_http_and_disk', default=False, 
        description=_("Log http and disk"), help_text=_(u"optional: Log via http and on disk, default is false") 
    ),
    BooleanValue(SERVER_GROUP, 'log_b_leg', default=False, 
        description=_("Log b leg"), help_text=_(u"optional: if not present we do log the b leg true or false if we should create a cdr for the b leg of a call") 
    ),
    BooleanValue(SERVER_GROUP, 'prefix_a_leg', default=True, 
        description=_("Prefix a leg"), help_text=_(u'optional: if not present, all filenames are the uuid of the call true or false if a leg files are prefixed "a_"') 
    ),
    BooleanValue(SERVER_GROUP, 'encode', default=True, 
        description=_("Encode"), help_text=_(u"encode the post data may be true for url encoding, false for no encoding or base64 for base64 encoding") 
    ),
    BooleanValue(SERVER_GROUP, 'lighttpd', default=True, 
        description=_("Lighttpd"), help_text=_(u"optional: set to true to disable Expect: 100-continue lighttpd requires this setting") 
    ),
    StringValue(SERVER_GROUP, 'err_log', default='log/xml_cdr/', 
        description=_("Error Log DIR"), help_text=_(u"optional: full path to the error log dir for failed web posts if not specified its the same as log-dir, either an absolute path, a relative path assuming ${prefix}/logs or a blank or omitted value will default to ${prefix}/logs/xml_cdr") 
    ),
    BooleanValue(SERVER_GROUP, 'cdr_ca', default=True, 
        description=_("Disable CA"), help_text=_(u"optional: if enabled this will disable CA root certificate checks by libcurl note: default value is disabled. only enable if you want this!") 
    ),
    ModuleValue(SERVER_GROUP,
       'MODULE',
       description=_('Implementation module'),
       hidden=True,
       default = 'fsa.cdr') 
)

