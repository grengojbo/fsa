# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.gateway.models import *

class Migration:
    
    def forwards(self, orm):
        # Adding field 'SofiaGateway.direction'
        db.add_column('carrier_gateway', 'direction', orm['gateway.sofiagateway:direction'])
        
        # Adding field 'SofiaGateway.in_progress_calls'
        db.add_column('carrier_gateway', 'in_progress_calls', orm['gateway.sofiagateway:in_progress_calls'])
        
        # Adding field 'SofiaGateway.prov_url'
        db.add_column('carrier_gateway', 'prov_url', orm['gateway.sofiagateway:prov_url'])
        
        # Adding field 'SofiaGateway.descriptions'
        db.add_column('carrier_gateway', 'descriptions', orm['gateway.sofiagateway:descriptions'])
        
        # Adding field 'SofiaGateway.extension_in_contact'
        db.add_column('carrier_gateway', 'extension_in_contact', orm['gateway.sofiagateway:extension_in_contact'])
        
        # Adding field 'SofiaGateway.exten'
        db.add_column('carrier_gateway', 'exten', orm['gateway.sofiagateway:exten'])
        
        # Adding field 'SofiaGateway.register_transport'
        db.add_column('carrier_gateway', 'register_transport', orm['gateway.sofiagateway:register_transport'])
        
        # Adding field 'SofiaGateway.max_concurrent'
        db.add_column('carrier_gateway', 'max_concurrent', orm['gateway.sofiagateway:max_concurrent'])
        
        # Adding ManyToManyField 'SofiaGateway.acl'
        db.create_table('carrier_gateway_acl', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sofiagateway', models.ForeignKey(orm.SofiaGateway, null=False)),
            ('fsacl', models.ForeignKey(orm['acl.FSAcl'], null=False))
        ))
                
        # Deleting field 'SofiaGateway.extension'
        db.delete_column('carrier_gateway', 'extension_id')
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'SofiaGateway.direction'
        db.delete_column('carrier_gateway', 'direction')
        
        # Deleting field 'SofiaGateway.in_progress_calls'
        db.delete_column('carrier_gateway', 'in_progress_calls')
        
        # Deleting field 'SofiaGateway.prov_url'
        db.delete_column('carrier_gateway', 'prov_url')
        
        # Deleting field 'SofiaGateway.descriptions'
        db.delete_column('carrier_gateway', 'descriptions')
        
        # Deleting field 'SofiaGateway.extension_in_contact'
        db.delete_column('carrier_gateway', 'extension_in_contact')
        
        # Deleting field 'SofiaGateway.exten'
        db.delete_column('carrier_gateway', 'exten')
        
        # Deleting field 'SofiaGateway.register_transport'
        db.delete_column('carrier_gateway', 'register_transport')
        
        # Deleting field 'SofiaGateway.max_concurrent'
        db.delete_column('carrier_gateway', 'max_concurrent')
        
        # Dropping ManyToManyField 'SofiaGateway.acl'
        db.delete_table('carrier_gateway_acl')
        
        # Adding field 'SofiaGateway.extension'
        db.add_column('carrier_gateway', 'extension', orm['gateway.sofiagateway:extension'])
        
    
    
    models = {
        'acl.fsacl': {
            'Meta': {'db_table': "'fs_acl'"},
            'acl_default': ('django.db.models.fields.CharField', [], {'default': "'deny'", 'max_length': '5'}),
            'acl_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'dialplan.context': {
            'default_context': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'gateway.sofiagateway': {
            'Meta': {'db_table': "'carrier_gateway'"},
            'acl': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['acl.FSAcl']"}),
            'caller_id_in_from': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dialplan.Context']", 'blank': 'True'}),
            'descriptions': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'expire_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60', 'null': 'True'}),
            'exten': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'extension_in_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'from_domain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'from_user': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_progress_calls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'lcr_format': ('django.db.models.fields.CharField', [], {'default': "'digits,name,rate,other,date_start,date_end'", 'max_length': '200', 'blank': 'True'}),
            'max_concurrent': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "'pass'", 'max_length': '25'}),
            'ping': ('django.db.models.fields.PositiveIntegerField', [], {'default': '25', 'null': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'prov_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'proxy': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'realm': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'register': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'register_proxy': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'register_transport': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'retry_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '30', 'null': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'default': "'pass'", 'max_length': '25'})
        }
    }
    
    complete_apps = ['gateway']
