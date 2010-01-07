# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.numberplan.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'NumberPlan.status'
        db.add_column('number_plan', 'status', orm['numberplan.numberplan:status'])
        
        # Adding field 'NumberPlan.date_active'
        db.add_column('number_plan', 'date_active', orm['numberplan.numberplan:date_active'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'NumberPlan.status'
        db.delete_column('number_plan', 'status')
        
        # Deleting field 'NumberPlan.date_active'
        db.delete_column('number_plan', 'date_active')
        
    
    
    models = {
        'numberplan.numberplan': {
            'Meta': {'db_table': "'number_plan'"},
            'date_active': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'enables': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nt': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'max_length': '1'}),
            'phone_number': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1'})
        }
    }
    
    complete_apps = ['numberplan']
