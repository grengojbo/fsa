# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.server.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Conf'
        db.create_table('server_conf', (
            ('id', orm['server.Conf:id']),
            ('name', orm['server.Conf:name']),
            ('enabled', orm['server.Conf:enabled']),
            ('xml_conf', orm['server.Conf:xml_conf']),
        ))
        db.send_create_signal('server', ['Conf'])
        
        # Adding model 'Server'
        db.create_table('server', (
            ('id', orm['server.Server:id']),
            ('name', orm['server.Server:name']),
            ('listen_ip', orm['server.Server:listen_ip']),
            ('listen_port', orm['server.Server:listen_port']),
            ('password', orm['server.Server:password']),
            ('sql_name', orm['server.Server:sql_name']),
            ('sql_login', orm['server.Server:sql_login']),
            ('sql_password', orm['server.Server:sql_password']),
            ('ssh_user', orm['server.Server:ssh_user']),
            ('ssh_password', orm['server.Server:ssh_password']),
            ('ssh_host', orm['server.Server:ssh_host']),
            ('enabled', orm['server.Server:enabled']),
        ))
        db.send_create_signal('server', ['Server'])
        
        # Adding model 'SipProfile'
        db.create_table('sip_profile', (
            ('id', orm['server.SipProfile:id']),
            ('name', orm['server.SipProfile:name']),
            ('server', orm['server.SipProfile:server']),
            ('enabled', orm['server.SipProfile:enabled']),
            ('proxy_media', orm['server.SipProfile:proxy_media']),
            ('ext_rtp_ip', orm['server.SipProfile:ext_rtp_ip']),
            ('ext_sip_ip', orm['server.SipProfile:ext_sip_ip']),
            ('domain', orm['server.SipProfile:domain']),
            ('rtp_ip', orm['server.SipProfile:rtp_ip']),
            ('sip_ip', orm['server.SipProfile:sip_ip']),
            ('sip_port', orm['server.SipProfile:sip_port']),
            ('accept_blind_reg', orm['server.SipProfile:accept_blind_reg']),
            ('codec_prefs', orm['server.SipProfile:codec_prefs']),
            ('context', orm['server.SipProfile:context']),
            ('other_param', orm['server.SipProfile:other_param']),
            ('comments', orm['server.SipProfile:comments']),
        ))
        db.send_create_signal('server', ['SipProfile'])
        
        # Adding model 'Alias'
        db.create_table('sip_alias', (
            ('id', orm['server.Alias:id']),
            ('name', orm['server.Alias:name']),
        ))
        db.send_create_signal('server', ['Alias'])
        
        # Adding ManyToManyField 'SipProfile.alias'
        db.create_table('alias_many', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sipprofile', models.ForeignKey(orm.SipProfile, null=False)),
            ('alias', models.ForeignKey(orm.Alias, null=False))
        ))
        
        # Adding ManyToManyField 'SipProfile.gateway'
        db.create_table('server_gateway', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sipprofile', models.ForeignKey(orm.SipProfile, null=False)),
            ('sofiagateway', models.ForeignKey(orm['gateway.SofiaGateway'], null=False))
        ))
        
        # Creating unique_together for [name, server] on SipProfile.
        db.create_unique('sip_profile', ['name', 'server_id'])
        
    
    
    def backwards(self, orm):
        
        # Deleting unique_together for [name, server] on SipProfile.
        db.delete_unique('sip_profile', ['name', 'server_id'])
        
        # Deleting model 'Conf'
        db.delete_table('server_conf')
        
        # Deleting model 'Server'
        db.delete_table('server')
        
        # Deleting model 'SipProfile'
        db.delete_table('sip_profile')
        
        # Deleting model 'Alias'
        db.delete_table('sip_alias')
        
        # Dropping ManyToManyField 'SipProfile.alias'
        db.delete_table('alias_many')
        
        # Dropping ManyToManyField 'SipProfile.gateway'
        db.delete_table('server_gateway')
        
    
    
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
            'xml_conf': ('django.db.models.fields.XMLField', [], {})
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
