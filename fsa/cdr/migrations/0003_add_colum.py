# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Cdr.nibble_account'
        db.add_column(u'cdr', 'nibble_account', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Adding field 'Cdr.sip_received_ip'
        db.add_column(u'cdr', 'sip_received_ip', self.gf('django.db.models.fields.IPAddressField')(default='127.0.0.1', max_length=15), keep_default=False)

        # Adding field 'Cdr.number_alias'
        db.add_column(u'cdr', 'number_alias', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True), keep_default=False)

        # Adding field 'Cdr.lcr_carrier'
        db.add_column(u'cdr', 'lcr_carrier', self.gf('django.db.models.fields.CharField')(default='local', max_length=50), keep_default=False)

        # Adding field 'Cdr.direction'
        db.add_column(u'cdr', 'direction', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Cdr.nibble_account'
        db.delete_column(u'cdr', 'nibble_account')

        # Deleting field 'Cdr.sip_received_ip'
        db.delete_column(u'cdr', 'sip_received_ip')

        # Deleting field 'Cdr.number_alias'
        db.delete_column(u'cdr', 'number_alias')

        # Deleting field 'Cdr.lcr_carrier'
        db.delete_column(u'cdr', 'lcr_carrier')

        # Deleting field 'Cdr.direction'
        db.delete_column(u'cdr', 'direction')


    models = {
        'cdr.cdr': {
            'Meta': {'object_name': 'Cdr', 'db_table': "u'cdr'"},
            'accountcode': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'answer_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'billsec': ('django.db.models.fields.IntegerField', [], {}),
            'caller_id_name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'caller_id_number': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'destination_number': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'direction': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'end_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'hangup_cause': ('django.db.models.fields.CharField', [], {'max_length': '135'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcr_carrier': ('django.db.models.fields.CharField', [], {'default': "'local'", 'max_length': '50'}),
            'nibble_account': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'number_alias': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'read_codec': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sip_received_ip': ('django.db.models.fields.IPAddressField', [], {'default': "'127.0.0.1'", 'max_length': '15'}),
            'start_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '108'}),
            'write_codec': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['cdr']
