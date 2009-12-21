# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.dialplan.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Extension'
        db.create_table('dialplan_extension', (
            ('id', orm['dialplan.Extension:id']),
            ('name', orm['dialplan.Extension:name']),
            ('continue_on', orm['dialplan.Extension:continue_on']),
            ('context', orm['dialplan.Extension:context']),
        ))
        db.send_create_signal('dialplan', ['Extension'])
        
        # Adding model 'Context'
        db.create_table('dialplan_context', (
            ('id', orm['dialplan.Context:id']),
            ('name', orm['dialplan.Context:name']),
            ('default_context', orm['dialplan.Context:default_context']),
        ))
        db.send_create_signal('dialplan', ['Context'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Extension'
        db.delete_table('dialplan_extension')
        
        # Deleting model 'Context'
        db.delete_table('dialplan_context')
        
    
    
    models = {
        'dialplan.context': {
            'default_context': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'dialplan.extension': {
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dialplan.Context']"}),
            'continue_on': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        }
    }
    
    complete_apps = ['dialplan']
