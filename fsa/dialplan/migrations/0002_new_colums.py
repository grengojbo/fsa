# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.dialplan.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Extension.desc'
        db.add_column('dialplan_extension', 'desc', orm['dialplan.extension:desc'])
        
        # Adding field 'Extension.actions_xml'
        db.add_column('dialplan_extension', 'actions_xml', orm['dialplan.extension:actions_xml'])
        
        # Adding field 'Extension.dest_num'
        db.add_column('dialplan_extension', 'dest_num', orm['dialplan.extension:dest_num'])
        
        # Adding field 'Extension.enabled'
        db.add_column('dialplan_extension', 'enabled', orm['dialplan.extension:enabled'])
        
        # Adding field 'Extension.priority_position'
        db.add_column('dialplan_extension', 'priority_position', orm['dialplan.extension:priority_position'])
        
        # Adding field 'Extension.is_temporary'
        db.add_column('dialplan_extension', 'is_temporary', orm['dialplan.extension:is_temporary'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Extension.desc'
        db.delete_column('dialplan_extension', 'desc')
        
        # Deleting field 'Extension.actions_xml'
        db.delete_column('dialplan_extension', 'actions_xml')
        
        # Deleting field 'Extension.dest_num'
        db.delete_column('dialplan_extension', 'dest_num')
        
        # Deleting field 'Extension.enabled'
        db.delete_column('dialplan_extension', 'enabled')
        
        # Deleting field 'Extension.priority_position'
        db.delete_column('dialplan_extension', 'priority_position')
        
        # Deleting field 'Extension.is_temporary'
        db.delete_column('dialplan_extension', 'is_temporary')
        
    
    
    models = {
        'dialplan.context': {
            'default_context': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'dialplan.extension': {
            'actions_xml': ('django.db.models.fields.XMLField', [], {'default': "''"}),
            'continue_on': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'default': "'welcome message'", 'max_length': '250'}),
            'dest_num': ('django.db.models.fields.CharField', [], {'default': "'^neoconf[-]?([0-9]*)$'", 'max_length': '75'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_temporary': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'priority_position': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }
    
    complete_apps = ['dialplan']
