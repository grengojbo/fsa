# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.directory.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Endpoint.uid'
        # (to signature: django.db.models.fields.CharField(max_length=12, unique=True))
        db.alter_column('endpoints', 'uid', orm['directory.endpoint:uid'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Endpoint.uid'
        # (to signature: django.db.models.fields.PositiveIntegerField(unique=True))
        db.alter_column('endpoints', 'uid', orm['directory.endpoint:uid'])
        
    
    
    models = {
        'acl.fsacl': {
            'Meta': {'db_table': "'fs_acl'"},
            'acl_default': ('django.db.models.fields.CharField', [], {'default': "'deny'", 'max_length': '5'}),
            'acl_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dialplan.context': {
            'default_context': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'extension': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dialplan.Extension']", 'null': 'True', 'blank': 'True'}),
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
            'is_condition': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_temporary': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'priority_position': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'directory.endpoint': {
            'Meta': {'db_table': "'endpoints'"},
            'accountcode': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'sip number'", 'max_length': '255', 'blank': 'True'}),
            'effective_caller_id_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_registered': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_registered': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'sip_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['server.SipProfile']"}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '12', 'unique': 'True'}),
            'user_context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dialplan.Context']"})
        },
        'directory.fsgroup': {
            'Meta': {'db_table': "'endpoints_group'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.Endpoint']", 'blank': 'True'})
        },
        'directory.sipregistration': {
            'Meta': {'db_table': "'sip_reg'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'sip_auth_cnonce': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'sip_auth_method': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sip_auth_nonce': ('django.db.models.fields.CharField', [], {'max_length': '36', 'unique': 'True'}),
            'sip_auth_qop': ('django.db.models.fields.CharField', [], {'default': "'auth'", 'max_length': '100'}),
            'sip_auth_realm': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sip_auth_response': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'sip_auth_uri': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sip_auth_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sip_contact_host': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sip_contact_user': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sip_from_host': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sip_from_user': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sip_request_host': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sip_to_host': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sip_to_user': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sip_user_agent': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Endpoint']"})
        },
        'gateway.sofiagateway': {
            'Meta': {'db_table': "'carrier_gateway'"},
            'acl': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['acl.FSAcl']", 'null': 'True', 'blank': 'True'}),
            'caller_id_in_from': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'default': '2', 'to': "orm['dialplan.Context']"}),
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
        },
        'server.alias': {
            'Meta': {'db_table': "'sip_alias'"},
            'alias_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '50'})
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
            'ssh_user': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        },
        'server.sipprofile': {
            'Meta': {'unique_together': "(('name', 'server'),)", 'db_table': "'sip_profile'"},
            'accept_blind_reg': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'alias': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['server.Alias']", 'blank': 'True'}),
            'codec_prefs': ('django.db.models.fields.CharField', [], {'default': "'G729,PCMU,GSM'", 'max_length': '100'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dialplan.Context']", 'blank': 'True'}),
            'default_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'ext_rtp_ip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ext_sip_ip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gateway': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['gateway.SofiaGateway']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'internal'", 'max_length': '50'}),
            'no_view_param': ('django.db.models.fields.XMLField', [], {'default': "'<!-- no view -->'"}),
            'other_param': ('django.db.models.fields.XMLField', [], {'blank': 'True'}),
            'outbound_codec_prefs': ('django.db.models.fields.CharField', [], {'default': "'G729,PCMU,GSM'", 'max_length': '100'}),
            'proxy_media': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'rtp_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'default': '2', 'related_name': "'sfs'", 'to': "orm['server.Server']"}),
            'sip_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'sip_port': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5060'})
        }
    }
    
    complete_apps = ['directory']
