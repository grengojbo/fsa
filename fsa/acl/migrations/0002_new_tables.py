# -*- coding: UTF-8 -*-

from south.db import db
from django.db import models
from fsa.acl.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'FSAclNode'
        db.create_table('fs_acl_node', (
            ('id', orm['acl.fsaclnode:id']),
            ('acl', orm['acl.fsaclnode:acl']),
            ('enabled', orm['acl.fsaclnode:enabled']),
            ('node_type', orm['acl.fsaclnode:node_type']),
            ('node', orm['acl.fsaclnode:node']),
            ('node_val', orm['acl.fsaclnode:node_val']),
        ))
        db.send_create_signal('acl', ['FSAclNode'])
        
        # Adding model 'AclNetworkList'
        db.create_table('fs_acl_network', (
            ('id', orm['acl.aclnetworklist:id']),
            ('name', orm['acl.aclnetworklist:name']),
        ))
        db.send_create_signal('acl', ['AclNetworkList'])
        
        # Adding ManyToManyField 'AclNetworkList.acl'
        db.create_table('fs_acl_network_acl', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aclnetworklist', models.ForeignKey(orm.AclNetworkList, null=False)),
            ('fsacl', models.ForeignKey(orm.FSAcl, null=False))
        ))
        
        # Adding field 'FSAcl.acl_type'
        db.add_column('fs_acl', 'acl_type', orm['acl.fsacl:acl_type'])
        
        # Deleting field 'FSAcl.acl_val'
        db.delete_column('fs_acl', 'acl_val')
        
        # Deleting field 'FSAcl.server'
        db.delete_column('fs_acl', 'server_id')
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'FSAclNode'
        db.delete_table('fs_acl_node')
        
        # Deleting model 'AclNetworkList'
        db.delete_table('fs_acl_network')
        
        # Dropping ManyToManyField 'AclNetworkList.acl'
        db.delete_table('fs_acl_network_acl')
        
        # Deleting field 'FSAcl.acl_type'
        db.delete_column('fs_acl', 'acl_type')
        
        # Adding field 'FSAcl.acl_val'
        db.add_column('fs_acl', 'acl_val', orm['acl.fsacl:acl_val'])
        
        # Adding field 'FSAcl.server'
        db.add_column('fs_acl', 'server', orm['acl.fsacl:server'])
        
    
    
    models = {
        'acl.aclnetworklist': {
            'Meta': {'db_table': "'fs_acl_network'"},
            'acl': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['acl.FSAcl']"}),
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
