# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Lcr.country_code'
        db.add_column('lcr', 'country_code', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Lcr.site'
        db.add_column('lcr', 'site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Lcr.country_code'
        db.delete_column('lcr', 'country_code')

        # Deleting field 'Lcr.site'
        db.delete_column('lcr', 'site_id')


    models = {
        'acl.fsacl': {
            'Meta': {'object_name': 'FSAcl', 'db_table': "'fs_acl'"},
            'acl_default': ('django.db.models.fields.CharField', [], {'default': "'deny'", 'max_length': '5'}),
            'acl_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'dialplan.context': {
            'Meta': {'object_name': 'Context'},
            'default_context': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'extension': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exten'", 'blank': 'True', 'null': 'True', 'to': "orm['dialplan.Extension']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'dialplan.extension': {
            'Meta': {'object_name': 'Extension'},
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
        'gateway.sofiagateway': {
            'Meta': {'object_name': 'SofiaGateway', 'db_table': "'carrier_gateway'"},
            'acl': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'gateway_acl'", 'blank': 'True', 'null': 'True', 'to': "orm['acl.FSAcl']"}),
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
        'lcr.lcr': {
            'Meta': {'object_name': 'Lcr', 'db_table': "'lcr'"},
            'carrier_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gateway.SofiaGateway']"}),
            'country_code': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'digits': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcr_profile': ('django.db.models.fields.CharField', [], {'max_length': '96', 'blank': 'True'}),
            'lead_strip': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'quality': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'rate': ('django.db.models.fields.FloatField', [], {}),
            'reliability': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['sites.Site']"}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'trail_strip': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['lcr']
