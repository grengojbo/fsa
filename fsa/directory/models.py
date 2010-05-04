# -*- mode: python; coding: utf-8; -*-
from django.db import models
#from lib.composition import CompositionField, AttributesAggregation, ChildsAggregation, ForeignAttribute
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from fsa.dialplan.models import Context
from fsa.server.models import SipProfile
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from fsa.directory.managers import EndpointManager, SipRegistrationManager
import config
from livesettings import ConfigurationSettings, config_value, config_choice_values
#from .managers import 
import logging
import datetime
import signals


log = logging.getLogger('fsa.directory.models')

__author__ = '$Author: $'
__revision__ = '$Revision: $'

"""
http://wiki.freeswitch.org/wiki/Mod_xml_curl#bindings.3D.22directory.22
"""

# Create your models here.
PHONE_TYPES = (('S', _(u'SIP Soft Phone')),
               ('P', _(u'SIP Phone')),
               ('F', _(u'Fax')),
               ('H', _(u'H.323 Phone')),
            )

class Endpoint(models.Model):
    #uid = models.CharField(max_length=100)
    uid = models.CharField(_(u'Phone Number'), max_length=12, unique=True, blank=True)
    phone_type = models.CharField(_(u'Type'), max_length=1, choices=PHONE_TYPES, default='S')
    password = models.CharField(_(u'Password'), max_length=6, blank=True)
    accountcode = models.ForeignKey(User)
    user_context = models.ForeignKey(Context)
    sip_profile = models.ForeignKey(SipProfile)
    effective_caller_id_name = models.CharField(_(u'Caller id Name'), max_length=255, blank=True)
    enable = models.BooleanField(_(u'Enable'), default=True)
    # is this endpoint currently registered?
    is_registered = models.BooleanField(default=False)
    # the time this endpoint last registered
    last_registered = models.DateTimeField(null=True, blank=True)
    # the ip address it has for its contact field
    #contact_addr = models.CharField(maxlength=100, blank=True)
    site = models.ForeignKey(Site, default=1, verbose_name=_('Site'))
    description = models.CharField(_(u'Description'), max_length=255, blank=True, default='sip number')
    other_param = models.XMLField(_(u'Other Params'), blank=True, null=True, default='<!-- other param -->')
    other_variable = models.XMLField(_(u'Other Variables'), blank=True, null=True, default='<!-- other variable -->')

    objects = EndpointManager()

    #def get_extensions(self):
    #    return self.extension_set.all()

    def delete(self, *args, **kwargs):
        # TODO work signal 'Signal' object is not callable
        log.debug('delete endpoint: %s' % self.uid)
        #signals.endpoint_delete('EndpointDelete', endpoint=self.uid)
        super(Endpoint, self).delete()
    
    def save(self, *args, **kwargs):
            
        if not self.uid:
            try:
                from fsa.numberplan.models import NumberPlan
                self.uid = NumberPlan.objects.lphonenumber()
            except:
                self.uid = '0000000'
        if not self.password:
            self.password = User.objects.make_random_password(6, "0123456789")
        if not self.effective_caller_id_name:
            self.effective_caller_id_name = self.uid
        if not self.pk:
            log.debug('new endpoint')
            signals.endpoint_create.send(self, endpoint=self)
        else:
            old_endpoint = Endpoint.objects.get(pk=self.pk)
            log.debug('change endpoint')
            signals.endpoint_change.send(self, endpoint=self, old_endpoint=old_endpoint)
        log.debug('save endpoint: %s' % self.uid)
        super(Endpoint, self).save(*args, **kwargs)
        
    class Meta:
        db_table = 'endpoints'
        verbose_name = _(u'Endpoint')
        verbose_name_plural = _(u'Endpoints')

    def __unicode__(self):
        return str(self.uid)

#class ExternalPhone(PhoneNumber):
#    def __unicode__(self):
#        return self.uid+'('+self.description+')'

#class FSUser(PhoneNumber):
#    "FreeSWITCH user"
#    password = m.CharField(max_length=255)
#    effective_caller_id_number = m.CharField(max_length=255)
#    mailbox = m.CharField(max_length=255)
#    mailbox_pwd = m.CharField(max_length=255)
#    def __unicode__(self):
#        return self.uid + '/' + self.user_context.name

#class Variable(m.Model):
#    "Variable, in fact - type of variable"
#    name = m.CharField(max_length=255)
#    is_param = m.BooleanField()
#    def __unicode__(self):
#        return self.name+' ('+['var','param'][int(self.is_param)]+')'

#class FSUVariable(m.Model):
#    variable = m.ForeignKey(Variable)
#    value = m.CharField(max_length=255)
#    user = m.ForeignKey(FSUser)
#    def __unicode__(self):
#        return self.variable.name+' = '+self.value

class SipRegistration(models.Model):
    domain = models.CharField(_('Domain'), max_length=100)
    user = models.ForeignKey(Endpoint)
    ip = models.IPAddressField(_('IP Adress'))
    #section = 'directory'
    #hostname = 'grengo.colocall.net'
    sip_auth_username = models.CharField(_('User'), max_length=50)
    #sip_auth_nc = models.CharField(_('NC'), max_length=8)
    # default='00000001')
    sip_auth_method = models.CharField(_('Method'), max_length=30)
    # default='REGISTER')
    sip_auth_nonce = models.CharField(_('Nonce'), max_length=36, unique=True)
    # default='e8c26e3e-1792-11de-ae36-af3bf0ae904b')
    sip_auth_qop = models.CharField(_('Qop'), max_length=100, default='auth')
    #sip_auth_realm=test.lincom3000.com.ua
    sip_auth_realm = models.CharField(_('Realm'), max_length=100)
    sip_auth_uri = models.CharField(_('uri'), max_length=100)
    #, default='sip:62.149.27.151')
    sip_auth_cnonce = models.CharField(_('Cnonce'), max_length=32)
    sip_auth_response = models.CharField(_('Response'), max_length=32)
    sip_user_agent = models.CharField(_('Agent'), max_length=250)
    sip_from_user = models.CharField(_('From User'), max_length=50)
    sip_from_host = models.CharField(_('From Host'), max_length=100)
    sip_to_user = models.CharField(_('To User'), max_length=50)
    sip_to_host = models.CharField(_('To Host'), max_length=100)
    sip_contact_user = models.CharField(_('Contact User'), max_length=50)
    sip_contact_host = models.CharField(_('Contact Host'), max_length=100)
    sip_request_host = models.CharField(_('Request Host'), max_length=100)
    
    #sip_profile=internal
    #sip_auth_nonce=426d4308-56e6-11df-8fab-cf38109feabb
    #sip_auth_uri=sip%3Atest.lincom3000.com.ua
    #sip_contact_user=380895900000
    #     &sip_contact_host=193.201.83.3
    #     &sip_to_user=380895900000
    #     &sip_to_host=test.lincom3000.com.ua
    #     &sip_from_user=380895900000
    #     &sip_from_host=test.lincom3000.com.ua
    #sip_request_host=test.lincom3000.com.ua
    #&sip_auth_qop=auth
    #&sip_auth_cnonce=VlLTGJWeNvIgt1QiWsQf9z-h4Sr8vCLa
    #&sip_auth_nc=00000001
    #&sip_auth_response=aca561ab4fc8a886fc7852165333bbfb
    #&sip_auth_method=REGISTER

    #tag_name = models.CharField(_(''), max_length=100, default='domain')
    #sip_profile = models.CharField(_('Profile'), max_length=100)
    #, default='internal')
    #action = models.CharField(_(''), max_length=100, default='sip_auth')
    #key_value = '62.149.27.151',
    #key_name = 'name'
    #key = models.CharField(_(''), max_length=100, default='id'
    objects = SipRegistrationManager()
    
    class Meta:
        db_table = 'sip_reg'
        verbose_name = _(u'Registration Endpoint')
        verbose_name_plural = _(u'Registration Endpoints')

    #def __unicode__(self):
    #    return self.name

class FSGroup(models.Model):
    """
    Group of FSUsers
    """
    name = models.CharField(_('Name'), max_length=50, unique=True)
    users = models.ManyToManyField(Endpoint, blank=True, db_table='endpoint_to_groups')
    
    class Meta:
        db_table = 'endpoints_group'
        verbose_name = _(u'Group')
        verbose_name_plural = _(u'Groups')

    def __unicode__(self):
        return self.name

import listeners
listeners.start_listening()