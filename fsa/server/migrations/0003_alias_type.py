# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.server.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Alias.alias_type'
        db.add_column('sip_alias', 'alias_type', orm['server.alias:alias_type'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Alias.alias_type'
        db.delete_column('sip_alias', 'alias_type')
        
    
    
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
        },
        'server.alias': {
            'Meta': {'db_table': "'sip_alias'"},
            'alias_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '50'})
        },
        'server.conf': {
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'default': '2', 'to': "orm['server.Server']"}),
            'xml_conf': ('django.db.models.fields.XMLField', [], {})
        },
        'server.server': {
            'Meta': {'db_table': "'server'"},
            'acl': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['acl.FSAcl']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listen_acl': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'event_socket'", 'to': "orm['acl.FSAcl']"}),
            'listen_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'listen_port': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nat_map': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'server_version': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sql_login': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'sql_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'sql_password': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'ssh_host': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ssh_password': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'ssh_user': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        },
        'server.sipprofile': {
            'Meta': {'unique_together': "(('name', 'server'),)", 'db_table': "'sip_profile'"},
            'accept_blind_reg': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'alias': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['server.Alias']", 'blank': 'True'}),
            'codec_prefs': ('django.db.models.fields.CharField', [], {'default': "'G729,PCMU,GSM'", 'max_length': '100'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dialplan.Context']", 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'ext_rtp_ip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ext_sip_ip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gateway': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['gateway.SofiaGateway']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'internal'", 'max_length': '50'}),
            'other_param': ('django.db.models.fields.XMLField', [], {'blank': 'True'}),
            'proxy_media': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'rtp_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['server.Server']"}),
            'sip_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'sip_port': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5060'})
        }
    }
    
    complete_apps = ['server']
