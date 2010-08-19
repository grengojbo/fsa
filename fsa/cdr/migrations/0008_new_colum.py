# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Cdr.site_id'
        db.add_column(u'cdr', 'site_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=1), keep_default=False)

        # Adding field 'Cdr.gw_id'
        db.add_column(u'cdr', 'gw_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Adding field 'Cdr.gw'
        db.add_column(u'cdr', 'gw', self.gf('django.db.models.fields.CharField')(default='local', max_length=50), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Cdr.site_id'
        db.delete_column(u'cdr', 'site_id')

        # Deleting field 'Cdr.gw_id'
        db.delete_column(u'cdr', 'gw_id')

        # Deleting field 'Cdr.gw'
        db.delete_column(u'cdr', 'gw')


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
            'gw': ('django.db.models.fields.CharField', [], {'default': "'local'", 'max_length': '50'}),
            'gw_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
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
            'site_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'start_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '108'}),
            'write_codec': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['cdr']
