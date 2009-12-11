# -*- coding: UTF-8 -*-
from django.db import models
from django.conf import settings
from fsadmin.server.models import Server
from django.utils.translation import ugettext_lazy as _

#from .managers import 

__author__ = '$Author:$'
__revision__ = '$Revision:$'

#ACL_CHOICES = ( ('deny', _(u'Deny')), ('allow', _(u'Allow')),)
#TYPE_CHOICES = ( ('deny', _(u'Deny')), ('allow', _(u'Allow')),)

# Create your models here.
class FSAcl(models.Model):
    """
    """
    name = models.CharField(_(u'Name'), max_length=25)
    server = models.ForeignKey(Server)
    enabled = models.BooleanField(_(u'Enable'), default=True)
    #acl_default = models.CharField(_(u'Default Permission'), choices=ACL_CHOICES, max_length=5, default='deny')
    acl_val = models.XMLField(_(u'Value'), default='<node type="allow" domain="test.example.com"/>')
    #other_param = models.XMLField(_(u'Other Param'), blank=True)

    class Meta:
        db_table = 'fs_acl'
        verbose_name = _(u'ACL')
        verbose_name_plural = _(u'Acl Network List')

    def __unicode__(self):
        return self.name

#class AclNetworkList(models.Model):
#    """
#    """
#    acl = models.ForeignKey(FSAcl)
#    prem = models.CharField(_(u'Permission'), choices=ACL_CHOICES, max_length=5, default='allow')
#    type = models.CharField(_(u'Type'), choices=TYPE_CHOICES, max_length=5, default='allow')
#    val = models.CharField(_(u'Value'))
#
#    class Meta:
#        db_table = 'fs_acl'
#        verbose_name = _(u'ACL')
#        verbose_name_plural = _(u'Acl Network List')
#
#    def __unicode__(self):
#        return self.server.name
