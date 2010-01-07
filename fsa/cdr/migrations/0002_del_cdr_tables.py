# -*- mode: python; coding: utf-8; -*-

from south.db import db
from django.db import models
from fsa.cdr.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Deleting model 'conf'
        db.delete_table('cdr_conf')
        
    
    
    def backwards(self, orm):
        
        # Adding model 'conf'
        db.create_table('cdr_conf', (
            ('prefix_a_leg', orm['cdr.conf:prefix_a_leg']),
            ('name', orm['cdr.conf:name']),
            ('retries', orm['cdr.conf:retries']),
            ('passwd', orm['cdr.conf:passwd']),
            ('enabled', orm['cdr.conf:enabled']),
            ('lighttpd', orm['cdr.conf:lighttpd']),
            ('cdr_ca', orm['cdr.conf:cdr_ca']),
            ('log_b_leg', orm['cdr.conf:log_b_leg']),
            ('delay', orm['cdr.conf:delay']),
            ('err_log', orm['cdr.conf:err_log']),
            ('log_dir', orm['cdr.conf:log_dir']),
            ('url', orm['cdr.conf:url']),
            ('server', orm['cdr.conf:server']),
            ('id', orm['cdr.conf:id']),
            ('user', orm['cdr.conf:user']),
        ))
        db.send_create_signal('cdr', ['conf'])
        
    
    
    models = {
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
        }
    }
    
    complete_apps = ['cdr']
