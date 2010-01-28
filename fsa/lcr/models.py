# -*- mode: python; coding: utf-8; -*-
# 
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
#
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
#from django.contrib.auth.models import User
#from fsa.dialplan.models import Context
from fsa.lcr.managers import LcrManager
from fsa.core.managers import GenericManager
from fsa.gateway.models import SofiaGateway

#from .managers import 

__author__ = '$Author:$'
__revision__ = '$Revision:$'
__all__ = ['main', __revision__]


#class CarrierGateway(models.Model):
#    id = models.IntegerField(primary_key=True)
#    carrier_id = models.IntegerField(null=True, blank=True)
#    prefix = models.CharField(max_length=48)
#    suffix = models.CharField(max_length=48)
#    enabled = models.IntegerField()
#    class Meta:
#        db_table = u'carrier_gateway'

#class Carriers(models.Model):
#    id = models.IntegerField(primary_key=True)
#    carrier_name = models.CharField(max_length=765, blank=True)
#    enabled = models.IntegerField()
#    class Meta:
#        db_table = u'carriers'

class Lcr(models.Model):
    #id = models.IntegerField(primary_key=True)
    digits = models.CharField(_(u'Digits'), max_length=45, blank=True, help_text=_(u'matching digits'))
    # TODO: напрвление
    name = models.CharField(_(u'Country'), max_length=200, blank=True)
    rate = models.FloatField(_(u'Rate'))
    carrier_id = models.ForeignKey(SofiaGateway, help_text=_(u'which carrier for this entry'))
    lead_strip = models.IntegerField(_(u'Strip front'), default=0, help_text=_(u'how many digits to strip off front of passed in number'))
    trail_strip = models.IntegerField(_(u'Strip end'), default=0, help_text=_(u'how many digits to strip of end of passed in number'))
    prefix = models.CharField(_(u'Prefix'), max_length=100, blank=True, help_text=_(u'value to add to front of passed in numbe'))
    suffix = models.CharField(_(u'Suffix'), max_length=100, blank=True, help_text=_(u'vaulue to add to end of passed in number'))
    lcr_profile = models.CharField(_(u'LCR Profile'), max_length=96, blank=True)
    date_start = models.DateTimeField(_(u'Date Start'))
    date_end = models.DateTimeField(_(u'Date End'))
    quality = models.FloatField(_(u'Quality'), default=0, help_text=_(u'alternate field to order by'))
    reliability = models.FloatField(_(u'Reliability'), default=0, help_text=_(u'alternate field to order by'))
    enabled = models.BooleanField(_(u'Enable'), default=True)
    objects = LcrManager()
    active_objects = GenericManager( enabled = True ) # only active entries
    inactive_objects = GenericManager( enabled = False ) # only inactive entries

    class Meta:
        db_table = 'lcr'
        verbose_name = _(u'LCR')
        verbose_name_plural = _(u'LCRs')
        
    def __unicode__(self):
        return self.name
