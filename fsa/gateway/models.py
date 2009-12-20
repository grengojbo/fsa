# -*- mode: python; coding: utf-8; -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from fsa.gateway.managers import GatewayManager
from fsa.dialplan.models import Context, Extension

__author__ = '$Author: $'
__revision__ = '$Revision: $'
"""
SIP Provider Examples
http://wiki.freeswitch.org/wiki/Tested_Phone_Providers_Listing
"""

class SofiaGateway(models.Model):
    # TODO добавить
    #<param name="extension" value="sipmos"/>
    #  <param name="context" value="default"/>
    # gateway name
    name = models.CharField(_(u'Name'), max_length=50)
    # username for gateway login/authentication
    username = models.CharField(_(u'Username'), max_length=25, help_text=_(' username for gateway login/authentication'))
    # password for gateway login/authentication
    password = models.CharField(_(u'Password'), max_length=25, help_text=_('password for gateway login/authentication'))
    # auth realm: *optional* same as gateway name, if blank
    realm = models.CharField(_(u'Realm'), max_length=50, blank=True, help_text=_('auth realm: *optional* same as gateway name, if blank'))
    from_user = models.CharField(_(u'From User'), max_length=50, blank=True, help_text=_(u'username to use in from: *optional* same as  username, if blank'))
    # domain to use in from: *optional* same as  realm, if blank
    from_domain = models.CharField(_(u'From Domain'), max_length=50, blank=True, help_text=_(u'domain to use in from: *optional* same as  realm, if blank'))
    # extension for inbound calls: *optional* same as username, if blank
    extension = models.CharField(_(u'Extension'), max_length=50, blank=True, help_text=_('extension for inbound calls: *optional* same as username, if blank'))
  # proxy host: *optional* same as realm, if blank
    proxy = models.CharField(_(u'Proxy'), max_length=50, blank=True, help_text=_(u'proxy host: *optional* same as realm, if blank'))
    register_proxy = models.CharField(_(u'Register Proxy'), max_length=50, blank=True, help_text=_(u'send register to this proxy: *optional* same as proxy, if blank'))
    # expire in seconds: *optional* 3600, if blank
    expire_seconds = models.PositiveIntegerField(_(u'Expire'), default=60, null=True, help_text=_(u'expire in seconds: *optional* 3600, if blank'))
    # register w/ the gateway?
    register = models.BooleanField(_(u'Register'), default=False)
    # How many seconds before a retry when a failure or timeout occurs -->
    retry_seconds = models.PositiveIntegerField(_(u'Retry'), default=30, null=True, help_text=_(u'How many seconds before a retry when a failure or timeout occurs'))
    # Use the callerid of an inbound call in the from field on outbound calls via this gateway
    # replace the INVITE from user with the channel's caller-id    
    caller_id_in_from = models.BooleanField(_(u'CallerId in From'), default=False, help_text=_(u'Use the callerid of an inbound call in the from field on outbound calls via this gateway'))
    ping = models.PositiveIntegerField(_(u'Ping'), default=25, null=True, help_text=_(u'send an options ping every x seconds, failure will unregister and/or mark it down'))
    prefix = models.CharField(_(u'Prefix'), max_length=100, blank=True, help_text=_(u'example: sofia/external/'))
    suffix = models.CharField(_(u'Suffix'), max_length=100, blank=True, help_text=_(u'example:@proxy.carrier2.net:5060'))
    enabled = models.BooleanField(_(u'Enable'), default=False)
    lcr_format = models.CharField(_(u'Lcr Format'), max_length=200, blank=True, default="digits,name,rate,other,date_start,date_end", help_text=_(u'Format file to load LCR'))
    extension = models.ForeignKey(Extension, default=1)
    context = models.ForeignKey(Context, blank=True)
    objects = GatewayManager()
    
    # sofia profile this gateway is part of
    #account = models.ForeignKey('Account')    
    # incoming/outgoing/both
    #direction = models.CharField(maxlength=20)
    # The maximum number of concurrent calls supported by this gw
    #max_concurrent = models.PositiveIntegerField()
    # The number of calls in progress
    #in_progress_calls = models.PositiveIntegerField(null=True)
    
    class Meta:
        db_table = 'carrier_gateway'
        verbose_name = _(u'Gateway')
        verbose_name_plural = _(u'Gateways')
    
    def __unicode__(self):
        if self.enabled:
            return self.name
        else:
            return "%s (%s)" % (self.name, _(u'disable'))
    