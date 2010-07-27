# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Cdr.lprice'
        db.add_column(u'cdr', 'lprice', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=18, decimal_places=4), keep_default=False)

        # Adding field 'Cdr.lprice_currency'
        db.add_column(u'cdr', 'lprice_currency', self.gf('django.db.models.fields.CharField')(default='USD', max_length=3), keep_default=False)

        # Adding field 'Cdr.lcr_name'
        db.add_column(u'cdr', 'lcr_name', self.gf('django.db.models.fields.CharField')(default='local', max_length=200), keep_default=False)

        # Adding field 'Cdr.lcr_digits'
        db.add_column(u'cdr', 'lcr_digits', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Adding field 'Cdr.procesed'
        db.add_column(u'cdr', 'procesed', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Cdr.lprice'
        db.delete_column(u'cdr', 'lprice')

        # Deleting field 'Cdr.lprice_currency'
        db.delete_column(u'cdr', 'lprice_currency')

        # Deleting field 'Cdr.lcr_name'
        db.delete_column(u'cdr', 'lcr_name')

        # Deleting field 'Cdr.lcr_digits'
        db.delete_column(u'cdr', 'lcr_digits')

        # Deleting field 'Cdr.procesed'
        db.delete_column(u'cdr', 'procesed')


    models = {
        'cdr.cdr': {
            'Meta': {'object_name': 'Cdr', 'db_table': "u'cdr'"},
            'accountcode': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'answer_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'billsec': ('django.db.models.fields.IntegerField', [], {}),
            'caller_id_name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'caller_id_number': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'cash': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '18', 'decimal_places': '2'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'destination_number': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'direction': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'end_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'hangup_cause': ('django.db.models.fields.CharField', [], {'max_length': '135'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcr_carrier': ('django.db.models.fields.CharField', [], {'default': "'local'", 'max_length': '50'}),
            'lcr_digits': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'lcr_name': ('django.db.models.fields.CharField', [], {'default': "'local'", 'max_length': '200'}),
            'lcr_rate': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '18', 'decimal_places': '4'}),
            'lprice': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '18', 'decimal_places': '4'}),
            'lprice_currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'marja': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '18', 'decimal_places': '2'}),
            'nibble_account': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'nibble_rate': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '18', 'decimal_places': '2'}),
            'number_alias': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'procesed': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1'}),
            'read_codec': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sip_received_ip': ('django.db.models.fields.IPAddressField', [], {'default': "'127.0.0.1'", 'max_length': '15'}),
            'start_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '108'}),
            'write_codec': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['cdr']
