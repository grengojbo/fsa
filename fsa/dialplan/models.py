# -*- mode: python; coding: utf-8; -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
#from users.models import PhoneNumber

#from .managers import 

__author__ = '$Author: $'
__revision__ = '$Revision: $'


# Create your models here.
class Context(models.Model):
    # TODO перенести default_context в настройки для сайта
    name = models.CharField(_(u'Name'), max_length=50, unique=True)
    default_context = models.BooleanField(_(u'Default'),default=False)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'dialplan_context'
        verbose_name = _(u'Dialplan Context')
        verbose_name_plural = _(u'Dialplan Contexts')
        
class Extension(models.Model):
    name = models.CharField(_(u'Name'), max_length=50, unique=True)
    continue_on = models.BooleanField(default=False)
    context = models.ForeignKey(Context)
    #pref = models.IntegerField()

    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'dialplan_extension'
        verbose_name = _(u'Dialplan Extension')
        verbose_name_plural = _(u'Dialplan Extensions')
        
#BREAK = (
#    ("on-false","on-false"),
#    ("on-true","on-true"),
#    ("always","always"),
#    ("never","never"),
#)

#class Condition(m.Model):
#    field = m.CharField(max_length=255)
#    expression = m.CharField(max_length=255)
#    break_on = m.CharField(max_length=10,choices=BREAK,default="on-false")
#    extension = m.ForeignKey(Extension)
#    pref = m.IntegerField()
#    def __unicode__(self):
#        return "%s === %s"%(self.field,self.expression)
#    class Meta:
#        ordering = ['pref']

#class DPApp(m.Model):
#    name = m.CharField(max_length=255)
#    def __unicode__(self):
#        return self.name

#def get_dpapp(app):
#    f = DPApp.objects.filter(name=app)
#    if f:
#        return f[0]
#    else:
#        new = DPApp(name=app)
#        new.save()
#        return new

#class Action(m.Model):
#    app = m.ForeignKey(DPApp)
#    condition = m.ForeignKey(Condition)
#    params = m.CharField(max_length=255)
#    anti = m.BooleanField()
#    pref = m.IntegerField()
#    def __unicode__(self):
#        return "%s(%s)"%(self.app.name,self.params)
#    class Meta:
#        ordering = ['pref']

