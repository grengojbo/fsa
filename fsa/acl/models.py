# -*- coding: UTF-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

#from .managers import 

__author__ = '$Author:$'
__revision__ = '$Revision:$'

ACL_CHOICES = ( ('deny', _(u'Deny')), ('allow', _(u'Allow')),)
TYPE_CHOICES = ( (0, _(u'SyStem')), (1, _(u'User')),)
NODE_CHOICES = ( ('cidr', _(u'Ip/Mask')), ('domain', _(u'Domain name')),)

     
# Create your models here.
class FSAcl(models.Model):
    """
    """
    name = models.CharField(_(u'Name'), max_length=25)
    enabled = models.BooleanField(_(u'Enable'), default=True)
    acl_default = models.CharField(_(u'Default Permission'), choices=ACL_CHOICES, max_length=5, default='deny')
    acl_type = models.PositiveSmallIntegerField(_(u'Type'), choices=TYPE_CHOICES, default=0)
    
    objects = models.Manager()
    
    class Meta:
        db_table = 'fs_acl'
        verbose_name = _(u'ACL')
        verbose_name_plural = _(u'Acls')

    @property
    def vacl(self):
        return '<list name="%s" default="%s">' % (self.name, self.acl_default)
    
    @property
    def nodes(self):
        return self.relnode.filter(enabled=True)
        
    def __unicode__(self):
        return self.name

class FSAclNode(models.Model):
    """
    This will traverse the directory adding all users 
	with the cidr= tag to this ACL, when this ACL matches
	the users variables and params apply as if they 
	digest authenticated.
    """
    # TODO добавить фильтр только системые
    acl = models.ForeignKey(FSAcl, verbose_name=u"Acl", related_name='relnode')
    enabled = models.BooleanField(_(u'Enabled'), default=True)
    node_type = models.CharField(_(u'Default Permission'), choices=ACL_CHOICES, max_length=5, default='deny')
    node = models.CharField(_(u'Default Permission'), choices=NODE_CHOICES, max_length=6, default='domain')
    node_val = models.CharField(_(u'Value'), default='test.example.com', max_length=100)

    class Meta:
        db_table = 'fs_acl_node'
    
    @property
    def vnode(self):
        return '<node type="%s" %s="%s"/>' % (self.node_type, self.node, self.node_val)
        
    def __unicode__(self):
        return self.vnode
        
class AclNetworkList(models.Model):
   """
   """
   # TODO bpvtybnm отображение FSAcl
   name = models.CharField(_(u'Name'), max_length=25)
   acl = models.ManyToManyField(FSAcl, related_name='acls')
   enabled = models.BooleanField(_(u'Enabled'), default=True)
   
   objects = models.Manager()
   
   class Meta:
       db_table = 'fs_acl_network'
       verbose_name = _(u'Acl Network List')
       verbose_name_plural = _(u'Acl Network Lists')

   def __unicode__(self):
        return self.name
