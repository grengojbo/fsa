# -*- coding: UTF-8 -*-

from south.db import db
from django.db import models
from fsa.acl.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'AclNetworkList.enabled'
        db.add_column('fs_acl_network', 'enabled', orm['acl.aclnetworklist:enabled'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'AclNetworkList.enabled'
        db.delete_column('fs_acl_network', 'enabled')
        
    
    
    models = {
        'acl.aclnetworklist': {
            'Meta': {'db_table': "'fs_acl_network'"},
            'acl': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['acl.FSAcl']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'acl.fsacl': {
            'Meta': {'db_table': "'fs_acl'"},
            'acl_default': ('django.db.models.fields.CharField', [], {'default': "'deny'", 'max_length': '5'}),
            'acl_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'acl.fsaclnode': {
            'Meta': {'db_table': "'fs_acl_node'"},
            'acl': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['acl.FSAcl']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.CharField', [], {'default': "'domain'", 'max_length': '5'}),
            'node_type': ('django.db.models.fields.CharField', [], {'default': "'deny'", 'max_length': '5'}),
            'node_val': ('django.db.models.fields.CharField', [], {'default': "'test.example.com'", 'max_length': '100'})
        }
    }
    
    complete_apps = ['acl']
