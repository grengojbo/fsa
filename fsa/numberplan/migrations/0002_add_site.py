# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'NumberPlan.site'
        db.add_column('number_plan', 'site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'NumberPlan.site'
        db.delete_column('number_plan', 'site_id')


    models = {
        'numberplan.numberplan': {
            'Meta': {'object_name': 'NumberPlan', 'db_table': "'number_plan'"},
            'date_active': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'enables': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nt': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'max_length': '1'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'unique': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['sites.Site']"}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['numberplan']
