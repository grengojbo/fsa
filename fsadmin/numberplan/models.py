# -*- coding: UTF-8 -*-
from django.db import models
from django.db.models import signals
from lib.composition import CompositionField, AttributesAggregation, ChildsAggregation, ForeignAttribute
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from fsadmin.dialplan.models import Context
from fsadmin.server.models import SipProfile
from fsadmin.numberplan.managers import NumberPlanManager

#from .managers import 

__author__ = '$Author: $'
__revision__ = '$Revision: $'

N_TYPES = ((0, _(u'Action')),
           (1,_(u'Default')),
           (2,_(u'Gold')),
        )

class NumberPlan(models.Model):
    """
    """
    phone_number = models.PositiveIntegerField(_(u'Phone Number'), unique=True)
    nt = models.PositiveSmallIntegerField(_(u'Type'), max_length=1, choices=N_TYPES, default=1, blank=False)
    enables = models.BooleanField(_(u'Enables'), default=False)
    objects = NumberPlanManager()

    class Meta:
        db_table = 'number_plan'
        verbose_name = _(u'Number Plan')
        verbose_name_plural = _(u'Number Plans')

    def __unicode__(self):
        return str(self.phone_number)

