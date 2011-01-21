# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'NumberGroup'
        db.create_table('number_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='default', max_length=50)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('number_start', self.gf('django.db.models.fields.IntegerField')(default=1000)),
            ('number_end', self.gf('django.db.models.fields.IntegerField')(default=1010)),
        ))
        db.send_create_signal('server', ['NumberGroup'])


    def backwards(self, orm):
        
        # Deleting model 'NumberGroup'
        db.delete_table('number_group')


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
        },
        'server.alias': {
            'Meta': {'object_name': 'Alias', 'db_table': "'sip_alias'"},
            'alias_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '50'})
        },
        'server.conf': {
            'Meta': {'object_name': 'Conf'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'default': '2', 'related_name': "'serverfs'", 'to': "orm['server.Server']"}),
            'xml_conf': ('django.db.models.fields.XMLField', [], {})
        },
        'server.csvbase': {
            'Meta': {'object_name': 'CsvBase', 'db_table': "'CsvBase'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'val': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'server.numbergroup': {
            'Meta': {'object_name': 'NumberGroup', 'db_table': "'number_group'"},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '50'}),
            'number_end': ('django.db.models.fields.IntegerField', [], {'default': '1010'}),
            'number_start': ('django.db.models.fields.IntegerField', [], {'default': '1000'})
        },
        'server.server': {
            'Meta': {'object_name': 'Server', 'db_table': "'server'"},
            'acl': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'server_acl'", 'symmetrical': 'False', 'to': "orm['acl.FSAcl']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listen_acl': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'event_socket'", 'to': "orm['acl.FSAcl']"}),
            'listen_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'listen_port': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nat_map': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'server_version': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'sipsites'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'sql_login': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'sql_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'sql_password': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'ssh_host': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ssh_user': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        },
        'server.sipprofile': {
            'Meta': {'unique_together': "(('name', 'server'),)", 'object_name': 'SipProfile', 'db_table': "'sip_profile'"},
            'accept_blind_reg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alias': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'relalias'", 'blank': 'True', 'db_table': "'alias_many'", 'to': "orm['server.Alias']"}),
            'codec_prefs': ('django.db.models.fields.CharField', [], {'default': "'G729,PCMU,GSM'", 'max_length': '100'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dialplan.Context']", 'blank': 'True'}),
            'default_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ext_rtp_ip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ext_sip_ip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gateway': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'relgw'", 'blank': 'True', 'db_table': "'server_gateway'", 'to': "orm['gateway.SofiaGateway']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'internal'", 'max_length': '50'}),
            'no_view_param': ('django.db.models.fields.XMLField', [], {'default': "'<!-- no view -->'"}),
            'other_param': ('django.db.models.fields.XMLField', [], {'blank': 'True'}),
            'outbound_codec_prefs': ('django.db.models.fields.CharField', [], {'default': "'G729,PCMU,GSM'", 'max_length': '100'}),
            'proxy_media': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rtp_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'default': '2', 'related_name': "'sfs'", 'to': "orm['server.Server']"}),
            'sip_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'sip_port': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5060'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'servsites'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sites.Site']"})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['server']
