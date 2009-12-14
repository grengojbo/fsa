# -*- coding: UTF-8 -*-

from south.db import db
from django.db import models
from fsa.acl.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'FSAcl'
        db.create_table('fs_acl', (
            ('id', orm['acl.FSAcl:id']),
            ('name', orm['acl.FSAcl:name']),
            ('server', orm['acl.FSAcl:server']),
            ('enabled', orm['acl.FSAcl:enabled']),
            ('acl_val', orm['acl.FSAcl:acl_val']),
        ))
        db.send_create_signal('acl', ['FSAcl'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'FSAcl'
        db.delete_table('fs_acl')
        
    
    
    models = {
        'acl.fsacl': {
            'Meta': {'db_table': "'fs_acl'"},
            'acl_val': ('django.db.models.fields.XMLField', [], {'default': '\'<node type="allow" domain="test.example.com"/>\''}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['server.Server']"})
        },
        'server.server': {
            'Meta': {'db_table': "'server'"},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listen_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'listen_port': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'sql_login': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'sql_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'sql_password': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'ssh_host': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ssh_password': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'ssh_user': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        }
    }
    
    complete_apps = ['acl']
