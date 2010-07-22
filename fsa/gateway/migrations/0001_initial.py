# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SofiaGateway'
        db.create_table('carrier_gateway', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descriptions', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('prov_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(default='pass', max_length=25)),
            ('password', self.gf('django.db.models.fields.CharField')(default='pass', max_length=25)),
            ('realm', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('from_user', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('from_domain', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exten', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('proxy', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('register_proxy', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('expire_seconds', self.gf('django.db.models.fields.PositiveIntegerField')(default=60, null=True)),
            ('register', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('retry_seconds', self.gf('django.db.models.fields.PositiveIntegerField')(default=30, null=True)),
            ('register_transport', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('caller_id_in_from', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('extension_in_contact', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('ping', self.gf('django.db.models.fields.PositiveIntegerField')(default=25, null=True)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('lcr_format', self.gf('django.db.models.fields.CharField')(default='digits,name,rate,other,date_start,date_end', max_length=200, blank=True)),
            ('context', self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['dialplan.Context'])),
            ('max_concurrent', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('in_progress_calls', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('direction', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2)),
        ))
        db.send_create_signal('gateway', ['SofiaGateway'])

        # Adding M2M table for field acl on 'SofiaGateway'
        db.create_table('carrier_gateway_acl', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sofiagateway', models.ForeignKey(orm['gateway.sofiagateway'], null=False)),
            ('fsacl', models.ForeignKey(orm['acl.fsacl'], null=False))
        ))
        db.create_unique('carrier_gateway_acl', ['sofiagateway_id', 'fsacl_id'])


    def backwards(self, orm):
        
        # Deleting model 'SofiaGateway'
        db.delete_table('carrier_gateway')

        # Removing M2M table for field acl on 'SofiaGateway'
        db.delete_table('carrier_gateway_acl')


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
            'extension': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'exten'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['dialplan.Extension']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'priority_position': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'gateway.sofiagateway': {
            'Meta': {'object_name': 'SofiaGateway', 'db_table': "'carrier_gateway'"},
            'acl': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'gateway_acl'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['acl.FSAcl']"}),
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
        }
    }

    complete_apps = ['gateway']
