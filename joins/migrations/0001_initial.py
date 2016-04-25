# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Join'
        db.create_table(u'joins_join', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='referral', null=True, to=orm['joins.Join'])),
            ('ref_id', self.gf('django.db.models.fields.CharField')(default='ABC', unique=True, max_length=20)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(default='ABC', max_length=128)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'joins', ['Join'])

        # Adding unique constraint on 'Join', fields ['email', 'ref_id']
        db.create_unique(u'joins_join', ['email', 'ref_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Join', fields ['email', 'ref_id']
        db.delete_unique(u'joins_join', ['email', 'ref_id'])

        # Deleting model 'Join'
        db.delete_table(u'joins_join')


    models = {
        u'joins.join': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'referral'", 'null': 'True', 'to': u"orm['joins.Join']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '128'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'unique': 'True', 'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['joins']