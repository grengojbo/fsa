# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.gateway.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'SofiaGateway'
        db.create_table('carrier_gateway', (
            ('id', orm['gateway.SofiaGateway:id']),
            ('name', orm['gateway.SofiaGateway:name']),
            ('username', orm['gateway.SofiaGateway:username']),
            ('password', orm['gateway.SofiaGateway:password']),
            ('realm', orm['gateway.SofiaGateway:realm']),
            ('from_user', orm['gateway.SofiaGateway:from_user']),
            ('from_domain', orm['gateway.SofiaGateway:from_domain']),
            ('proxy', orm['gateway.SofiaGateway:proxy']),
            ('register_proxy', orm['gateway.SofiaGateway:register_proxy']),
            ('expire_seconds', orm['gateway.SofiaGateway:expire_seconds']),
            ('register', orm['gateway.SofiaGateway:register']),
            ('retry_seconds', orm['gateway.SofiaGateway:retry_seconds']),
            ('caller_id_in_from', orm['gateway.SofiaGateway:caller_id_in_from']),
            ('ping', orm['gateway.SofiaGateway:ping']),
            ('prefix', orm['gateway.SofiaGateway:prefix']),
            ('suffix', orm['gateway.SofiaGateway:suffix']),
            ('enabled', orm['gateway.SofiaGateway:enabled']),
            ('lcr_format', orm['gateway.SofiaGateway:lcr_format']),
            ('extension', orm['gateway.SofiaGateway:extension']),
            ('context', orm['gateway.SofiaGateway:context']),
        ))
        db.send_create_signal('gateway', ['SofiaGateway'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'SofiaGateway'
        db.delete_table('carrier_gateway')
        
    
    
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
        },
        'gateway.sofiagateway': {
            'Meta': {'db_table': "'carrier_gateway'"},
            'caller_id_in_from': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dialplan.Context']", 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'expire_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60', 'null': 'True'}),
            'extension': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['dialplan.Extension']"}),
            'from_domain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'from_user': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcr_format': ('django.db.models.fields.CharField', [], {'default': "'digits,name,rate,other,date_start,date_end'", 'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'ping': ('django.db.models.fields.PositiveIntegerField', [], {'default': '25', 'null': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'proxy': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'realm': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'register': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'register_proxy': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'retry_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '30', 'null': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }
    
    complete_apps = ['gateway']
