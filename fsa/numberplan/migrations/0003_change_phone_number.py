# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.numberplan.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'NumberPlan.phone_number'
        # (to signature: django.db.models.fields.CharField(max_length=12, unique=True))
        db.alter_column('number_plan', 'phone_number', orm['numberplan.numberplan:phone_number'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'NumberPlan.phone_number'
        # (to signature: django.db.models.fields.PositiveIntegerField(unique=True))
        db.alter_column('number_plan', 'phone_number', orm['numberplan.numberplan:phone_number'])
        
    
    
    models = {
        'numberplan.numberplan': {
            'Meta': {'db_table': "'number_plan'"},
            'date_active': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'enables': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nt': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'max_length': '1'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'unique': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1'})
        }
    }
    
    complete_apps = ['numberplan']
