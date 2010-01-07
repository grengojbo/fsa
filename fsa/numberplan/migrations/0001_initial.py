# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.numberplan.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'NumberPlan'
        db.create_table('number_plan', (
            ('id', orm['numberplan.NumberPlan:id']),
            ('phone_number', orm['numberplan.NumberPlan:phone_number']),
            ('nt', orm['numberplan.NumberPlan:nt']),
            ('enables', orm['numberplan.NumberPlan:enables']),
        ))
        db.send_create_signal('numberplan', ['NumberPlan'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'NumberPlan'
        db.delete_table('number_plan')
        
    
    
    models = {
        'numberplan.numberplan': {
            'Meta': {'db_table': "'number_plan'"},
            'enables': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nt': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'max_length': '1'}),
            'phone_number': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        }
    }
    
    complete_apps = ['numberplan']
