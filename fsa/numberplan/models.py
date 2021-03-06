# -*- mode: python; coding: utf-8; -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from fsa.numberplan.managers import NumberPlanManager
from django.contrib.sites.models import Site
#from .managers import

__author__ = '$Author: $'
__revision__ = '$Revision: $'
N_STATUS = ((0, _(u'Free')),
           (1,_(u'Work')),
           (2,_(u'Park')),
           (3,_(u'Action')),
        )
N_TYPES = ((0, _(u'Partner')),
           (1,_(u'Default')),
           (2,_(u'Silver')),
           (3,_(u'Gold')),
           (4,_(u'Starting packet')),
        )

class NumberPlan(models.Model):
    """
    База номерного ресурса
    """
    phone_number = models.CharField(_(u'Phone Number'), max_length=12, unique=True)
    #models.PositiveIntegerField(_(u'Phone Number'), unique=True)
    nt = models.PositiveSmallIntegerField(_(u'Type'), max_length=1, choices=N_TYPES, default=1, blank=False)
    enables = models.BooleanField(_(u'Enables'), default=False)
    status = models.PositiveSmallIntegerField(_(u'Status'), max_length=1, choices=N_STATUS, default=0, blank=False)
    date_active = models.DateField(_(u'Activation Date'), blank=True, null=True)
    site = models.ForeignKey(Site, default=1, verbose_name=_(u'Site'))
    objects = NumberPlanManager()

    class Meta:
        db_table = 'number_plan'
        verbose_name = _(u'Number Plan')
        verbose_name_plural = _(u'Number Plans')

    def __unicode__(self):
        return self.phone_number

    @property
    def phone(self):
        return self.phone_number

import listeners
listeners.start_listening()
