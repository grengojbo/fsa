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
from django.utils.translation import ugettext_lazy as _
from fsa.lcr.managers import LcrManager
from bursar.fields import CurrencyField
from fsa.core.managers import GenericManager
from fsa.gateway.models import SofiaGateway
import datetime
from django.contrib.sites.models import Site
from decimal import Decimal


__author__ = '$Author:$'
__revision__ = '$Revision:$'
__all__ = ['main', __revision__]

OPERATOR_TYPE_CHOICES = (('F', _(u'Fixed')), ('M', _(u'Mobile')), ('N', _(u'Uncown')), ('S', _(u'Satelite')), ('V', _(u'VoIP')),)

#  DAYOFWEEK(NOW()) IN (1,2,3,4,6);

class Lcr(models.Model):
    #id = models.IntegerField(primary_key=True)
    digits = models.CharField(_(u'Digits'), max_length=45, blank=True, help_text=_(u'matching digits'))
    code = models.PositiveIntegerField(_(u'Code'), default=0)
    # TODO: напрвление
    name = models.CharField(_(u'Country'), max_length=200, blank=True)
    country_code = models.IntegerField(_(u'Country Code'), default=0)
    rate = CurrencyField(_("Subtotal"), max_digits=18, decimal_places=6, default=Decimal("0.0"), display_decimal=6)
    intrastate_rate = CurrencyField(_("rate for intrastate calls"), max_digits=18, decimal_places=6, default=Decimal("0.0"), display_decimal=6)
    intralata_rate = CurrencyField(_("rate for intralata calls"), max_digits=18, decimal_places=6, default=Decimal("0.0"), display_decimal=6)
    #price = MoneyField(max_digits=18, decimal_places=4, default=Money(0, Currency.objects.get_default()))
    price =  models.DecimalField('Price', default=Decimal("0"), max_digits=18, decimal_places=6)
    price_currency = models.CharField(_(u'Currency name'), max_length=3, default="USD")
    carrier_id = models.ForeignKey(SofiaGateway, help_text=_(u'which carrier for this entry'))
    lead_strip = models.IntegerField(_(u'Strip front'), default=0, help_text=_(u'how many digits to strip off front of passed in number'))
    trail_strip = models.IntegerField(_(u'Strip end'), default=0, help_text=_(u'how many digits to strip of end of passed in number'))
    prefix = models.CharField(_(u'Prefix'), max_length=100, blank=True, help_text=_(u'value to add to front of passed in numbe'))
    suffix = models.CharField(_(u'Suffix'), max_length=100, blank=True, help_text=_(u'vaulue to add to end of passed in number'))
    lcr_profile = models.CharField(_(u'LCR Profile'), max_length=96, blank=True)
    #date_start = models.DateTimeField(_(u'Date Start'), default=datetime.datetime.now())
    date_start = models.DateField(_(u'Date Start'), default=datetime.date.today())
    #date_end = models.DateTimeField(_(u'Date End'), default=datetime.datetime.max)
    quality = models.FloatField(_(u'Quality'), default=0, help_text=_(u'alternate field to order by'))
    reliability = models.FloatField(_(u'Reliability'), default=0, help_text=_(u'alternate field to order by'))
    cid = models.CharField(_(u'Callers caller id'), max_length=200, default='', blank=True, help_text=_(u'regular expression to modify the callers caller id number - channel variables are also valid when called from the dial plan'))
    enabled = models.BooleanField(_(u'Enable'), default=True)
    site = models.ForeignKey(Site, default=1, verbose_name=_('Site'))
    weeks = models.SmallIntegerField(_(u'Week'), default=0)
    operator_type = models.CharField(_(u'Тип'), choices=OPERATOR_TYPE_CHOICES, max_length=1, default='N')
    #tariff_id = models.IntegerField(_(u'ID Tariff'), default=1, help_text=_(u'Tariff Plan ID'))
    time_start = models.TimeField(_(u'Time Start'), default=datetime.datetime.strptime("00:00", "%H:%M"))
    time_end = models.TimeField(_(u'Time End'), default=datetime.datetime.strptime("23:59", "%H:%M"))
    objects = LcrManager()
    active_objects = GenericManager( enabled = True ) # only active entries
    inactive_objects = GenericManager( enabled = False ) # only inactive entries

    class Meta:
        db_table = 'lcr'
        verbose_name = _(u'LCR')
        verbose_name_plural = _(u'LCRs')

    @property
    def vprice(self):
        return "{0} {1}".format(self.price,self.price_currency)

    def __unicode__(self):
        return self.name

import listeners
listeners.start_listening()
