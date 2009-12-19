# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.server.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Server.listen_acl'
        db.add_column('server', 'listen_acl', orm['server.server:listen_acl'])
        
        # Adding field 'Server.nat_map'
        db.add_column('server', 'nat_map', orm['server.server:nat_map'])
        
        # Adding field 'Server.server_version'
        db.add_column('server', 'server_version', orm['server.server:server_version'])
        
        # Adding field 'Conf.server'
        db.add_column('server_conf', 'server', orm['server.conf:server'])
        
        # Adding ManyToManyField 'Server.acl'
        db.create_table('server_acl', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('server', models.ForeignKey(orm.Server, null=False)),
            ('fsacl', models.ForeignKey(orm['acl.FSAcl'], null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Server.listen_acl'
        db.delete_column('server', 'listen_acl_id')
        
        # Deleting field 'Server.nat_map'
        db.delete_column('server', 'nat_map')
        
        # Deleting field 'Server.server_version'
        db.delete_column('server', 'server_version')
        
        # Deleting field 'Conf.server'
        db.delete_column('server_conf', 'server_id')
        
        # Dropping ManyToManyField 'Server.acl'
        db.delete_table('server_acl')
        
    
    
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
