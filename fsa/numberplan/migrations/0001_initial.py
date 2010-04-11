# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'NumberPlan'
        db.create_table('number_plan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12)),
            ('nt', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1, max_length=1)),
            ('enables', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1)),
            ('date_active', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('numberplan', ['NumberPlan'])


    def backwards(self, orm):
        
        # Deleting model 'NumberPlan'
        db.delete_table('number_plan')


    models = {
        'numberplan.numberplan': {
            'Meta': {'object_name': 'NumberPlan', 'db_table': "'number_plan'"},
            'date_active': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'enables': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nt': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'max_length': '1'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1'})
        }
    }

    complete_apps = ['numberplan']
