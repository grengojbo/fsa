# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'SofiaGateway.destination_international'
        db.add_column('carrier_gateway', 'destination_international', self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True), keep_default=False)

        # Adding field 'SofiaGateway.destination_national'
        db.add_column('carrier_gateway', 'destination_national', self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'SofiaGateway.destination_international'
        db.delete_column('carrier_gateway', 'destination_international')

        # Deleting field 'SofiaGateway.destination_national'
        db.delete_column('carrier_gateway', 'destination_national')


    models = {
        'acl.fsacl': {
            'Meta': {'object_name': 'FSAcl', 'db_table': "'fs_acl'"},
            'acl_default': ('django.db.models.fields.CharField', [], {'default': "'deny'", 'max_length': '5'}),
            'acl_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'dialplan.context': {
            'Meta': {'object_name': 'Context'},
            'default_context': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'extension': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'exten'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['dialplan.Extension']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'dialplan.extension': {
            'Meta': {'object_name': 'Extension'},
            'actions_xml': ('django.db.models.fields.XMLField', [], {'default': "''"}),
            'continue_on': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'desc': ('django.db.models.fields.CharField', [], {'default': "'welcome message'", 'max_length': '250'}),
            'dest_num': ('django.db.models.fields.CharField', [], {'default': "'^neoconf[-]?([0-9]*)$'", 'max_length': '75'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_condition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_temporary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'priority_position': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'gateway.sofiagateway': {
            'Meta': {'object_name': 'SofiaGateway', 'db_table': "'carrier_gateway'"},
            'acl': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'gateway_acl'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['acl.FSAcl']"}),
            'caller_id_in_from': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'codec_string': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'default': '2', 'to': "orm['dialplan.Context']"}),
            'descriptions': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'destination_international': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'destination_national': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'destination_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'direction': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expire_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60', 'null': 'True'}),
            'exten': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'extension_in_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'from_domain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'from_user': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_progress_calls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'max_concurrent': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'money_nds': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '20'}),
            'money_period': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'money_time': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '60'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "'pass'", 'max_length': '25'}),
            'ping': ('django.db.models.fields.PositiveIntegerField', [], {'default': '25', 'null': 'True'}),
            'pref_international': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'pref_national': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'prefix_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'price_currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'prov_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'proxy': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'realm': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'register': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'register_proxy': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'register_transport': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'retry_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '30', 'null': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'default': "'pass'", 'max_length': '25'})
        }
    }

    complete_apps = ['gateway']
