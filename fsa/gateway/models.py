# -*- mode: python; coding: utf-8; -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from fsa.gateway.managers import GatewayManager
from fsa.dialplan.models import Context, Extension
from fsa.acl.models import FSAcl

__author__ = '$Author: $'
__revision__ = '$Revision: $'
"""
SIP Provider Examples
http://wiki.freeswitch.org/wiki/Tested_Phone_Providers_Listing

смотреть как реализовать для 
http://wiki.freeswitch.org/wiki/Provider_Configuration:_Brastel

"""
# TODO  смотреть как реализовать транк на провайдера

TRANSPORT_CHOICES = ( (0, _(u'None')), (1, _(u'UDP')), (2, _(u'TCP')),)
DIRECTION_CHOICES = ( (0, _(u'incoming')), (1, _(u'outgoing')), (2, _(u'both')),)

class SofiaGateway(models.Model):
    # TODO добавить
    #<param name="extension" value="sipmos"/>
    #  <param name="context" value="default"/>
    # gateway name
    name = models.CharField(_(u'Name'), max_length=50)
    descriptions = models.CharField(_(u'Descriptios'), blank=True, max_length=80, null=True)
    prov_url = models.URLField(_(u'Url Provider'), blank=True, verify_exists=True, null=True)
    # username for gateway login/authentication
    username = models.CharField(_(u'Username'), max_length=25, default='pass', help_text=_(' username for gateway login/authentication'))
    # password for gateway login/authentication
    password = models.CharField(_(u'Password'), max_length=25, default='pass', help_text=_('password for gateway login/authentication (pass - account password required by freeswitch but ignored)'))
    #password = models.CharField(_(u'Password'), max_length=25, blank=True, help_text=_('password for gateway login/authentication (pass - account password required by freeswitch but ignored)'))
    # auth realm: *optional* same as gateway name, if blank
    realm = models.CharField(_(u'Realm'), max_length=50, blank=True, help_text=_('auth realm: *optional* same as gateway name, if blank'))
    from_user = models.CharField(_(u'From User'), max_length=50, blank=True, help_text=_(u'username to use in from: *optional* same as  username, if blank'))
    # domain to use in from: *optional* same as  realm, if blank
    from_domain = models.CharField(_(u'From Domain'), max_length=50, blank=True, help_text=_(u'domain to use in from: *optional* same as  realm, if blank'))
    # extension for inbound calls: *optional* same as username, if blank
    exten = models.CharField(_(u'Extension'), max_length=50, blank=True, null=True, help_text=_('extension for inbound calls: *optional* same as username, if blank'))
  # proxy host: *optional* same as realm, if blank
    proxy = models.CharField(_(u'Proxy'), max_length=50, blank=True, help_text=_(u'proxy host: *optional* same as realm, if blank'))
    register_proxy = models.CharField(_(u'Register Proxy'), max_length=50, blank=True, help_text=_(u'send register to this proxy: *optional* same as proxy, if blank'))
    # expire in seconds: *optional* 3600, if blank
    expire_seconds = models.PositiveIntegerField(_(u'Expire'), default=60, null=True, help_text=_(u'expire in seconds: *optional* 3600, if blank'))
    # register w/ the gateway?
    register = models.BooleanField(_(u'Register'), default=False)
    # How many seconds before a retry when a failure or timeout occurs -->
    retry_seconds = models.PositiveIntegerField(_(u'Retry'), default=30, null=True, help_text=_(u'How many seconds before a retry when a failure or timeout occurs'))
    register_transport = models.PositiveSmallIntegerField(_(u'Register transport'), choices=TRANSPORT_CHOICES, default=0)
    # Use the callerid of an inbound call in the from field on outbound calls via this gateway
    # replace the INVITE from user with the channel's caller-id    
    caller_id_in_from = models.BooleanField(_(u'CallerId in From'), default=False, help_text=_(u'Use the callerid of an inbound call in the from field on outbound calls via this gateway'))
    # TODO add help text
    extension_in_contact = models.BooleanField(_(u'Extension in contac'), default=False)
    ping = models.PositiveIntegerField(_(u'Ping'), default=25, null=True, help_text=_(u'send an options ping every x seconds, failure will unregister and/or mark it down'))
    prefix = models.CharField(_(u'Prefix'), max_length=100, blank=True, help_text=_(u'example: sofia/external/'))
    suffix = models.CharField(_(u'Suffix'), max_length=100, blank=True, help_text=_(u'example:@proxy.carrier2.net:5060'))
    enabled = models.BooleanField(_(u'Enable'), default=False)
    lcr_format = models.CharField(_(u'Lcr Format'), max_length=200, blank=True, default="digits,name,rate,other,date_start,date_end", help_text=_(u'Format file to load LCR'))
    #extension = models.ForeignKey(Extension, blank=True, null=True)
    context = models.ForeignKey(Context, default=2)
    max_concurrent = models.PositiveIntegerField(_(u'Limit Calls'), default=0, help_text=_(u'The maximum number of concurrent calls supported by this gw (0 - is not limit)'))
    in_progress_calls = models.PositiveIntegerField(_(u'calls in progress'), default=0, help_text=_(u'The number of calls in progress (0 - is not limit)'))
    direction = models.PositiveSmallIntegerField(_(u'Direction'), choices=DIRECTION_CHOICES, default=2)
    acl = models.ManyToManyField(FSAcl, related_name='gateway_acl', blank=True, null=True)
    objects = GatewayManager()
    
    class Meta:
        db_table = 'carrier_gateway'
        verbose_name = _(u'Gateway')
        verbose_name_plural = _(u'Gateways')
    
    @property
    def status(self):
        """текущий статус"""
        # TODO добавить проверку статуса и какой пинг
        if self.register:
            return _(u'REGISTERED')
        else:
            return _(u'UnMonitored')
            
    @property
    def vrt(self):
        """
        преобразованиие 0 -none 1 - udp 2 - tcp
        для register_transport
        """
        # TODO сделать преобразованиие 0 -none 1 - udp 2 - tcp
        pass
        
    @property
    def vd(self):
        """
        преобразованиие 0 -incoming 1 - outgoing 2 - both
        для direction
        """
        # TODO сделать преобразованиие 0 -incoming 1 - outgoing 2 - both
        pass
            
    @property
    def vdescriptions(self):
        if self.prov_url:
            return "<a href='%s' target='new'>%s</a>" % (self.prov_url, self.descriptions) 
        else:
            return self.descriptions
            
    def __unicode__(self):
        if self.enabled:
            return self.name
        else:
            return "%s (%s)" % (self.name, _(u'disable'))
    