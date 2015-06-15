# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('django_workable_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('django_workable', ['Category'])

        # Adding model 'Position'
        db.create_table('django_workable_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job_shortcode', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_workable.Category'], null=True, blank=True)),
            ('job_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('detail_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('apply_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('django_workable', ['Position'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('django_workable_category')

        # Deleting model 'Position'
        db.delete_table('django_workable_position')


    models = {
        'django_workable.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'django_workable.position': {
            'Meta': {'object_name': 'Position'},
            'apply_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['django_workable.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'detail_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_shortcode': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'job_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['django_workable']