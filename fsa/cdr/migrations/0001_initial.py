# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.cdr.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Cdr'
        db.create_table(u'cdr', (
            ('id', orm['cdr.Cdr:id']),
            ('accountcode', orm['cdr.Cdr:accountcode']),
            ('caller_id_name', orm['cdr.Cdr:caller_id_name']),
            ('caller_id_number', orm['cdr.Cdr:caller_id_number']),
            ('destination_number', orm['cdr.Cdr:destination_number']),
            ('context', orm['cdr.Cdr:context']),
            ('start_timestamp', orm['cdr.Cdr:start_timestamp']),
            ('answer_timestamp', orm['cdr.Cdr:answer_timestamp']),
            ('end_timestamp', orm['cdr.Cdr:end_timestamp']),
            ('duration', orm['cdr.Cdr:duration']),
            ('billsec', orm['cdr.Cdr:billsec']),
            ('hangup_cause', orm['cdr.Cdr:hangup_cause']),
            ('uuid', orm['cdr.Cdr:uuid']),
            ('read_codec', orm['cdr.Cdr:read_codec']),
            ('write_codec', orm['cdr.Cdr:write_codec']),
        ))
        db.send_create_signal('cdr', ['Cdr'])
        
        # Adding model 'Conf'
        db.create_table(u'cdr_conf', (
            ('id', orm['cdr.Conf:id']),
            ('name', orm['cdr.Conf:name']),
            ('server', orm['cdr.Conf:server']),
            ('url', orm['cdr.Conf:url']),
            ('user', orm['cdr.Conf:user']),
            ('passwd', orm['cdr.Conf:passwd']),
            ('retries', orm['cdr.Conf:retries']),
            ('delay', orm['cdr.Conf:delay']),
            ('log_dir', orm['cdr.Conf:log_dir']),
            ('log_b_leg', orm['cdr.Conf:log_b_leg']),
            ('prefix_a_leg', orm['cdr.Conf:prefix_a_leg']),
            ('lighttpd', orm['cdr.Conf:lighttpd']),
            ('err_log', orm['cdr.Conf:err_log']),
            ('cdr_ca', orm['cdr.Conf:cdr_ca']),
            ('enabled', orm['cdr.Conf:enabled']),
        ))
        db.send_create_signal('cdr', ['Conf'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Cdr'
        db.delete_table(u'cdr')
        
        # Deleting model 'Conf'
        db.delete_table(u'cdr_conf')
        
    
    
    models = {
        'acl.fsacl': {
            'Meta': {'db_table': "'fs_acl'"},
            'acl_default': ('django.db.models.fields.CharField', [], {'default': "'deny'", 'max_length': '5'}),
            'acl_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'cdr.cdr': {
            'Meta': {'db_table': "u'cdr'"},
            'accountcode': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'answer_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'billsec': ('django.db.models.fields.IntegerField', [], {}),
            'caller_id_name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'caller_id_number': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'destination_number': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'end_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'hangup_cause': ('django.db.models.fields.CharField', [], {'max_length': '135'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read_codec': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'start_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '108'}),
            'write_codec': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'cdr.conf': {
            'cdr_ca': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'delay': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'err_log': ('django.db.models.fields.CharField', [], {'default': "'log/xml_cdr'", 'max_length': '240', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lighttpd': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'log_b_leg': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'log_dir': ('django.db.models.fields.CharField', [], {'max_length': '240', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'passwd': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'prefix_a_leg': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'retries': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['server.Server']"}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'http://localhost/cdr/set/'", 'max_length': '50'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
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
        }
    }
    
    complete_apps = ['cdr']
