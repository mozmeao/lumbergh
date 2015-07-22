# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Position.job_shortcode'
        db.delete_column('django_workable_position', 'job_shortcode')

        # Adding field 'Position.shortcode'
        db.add_column('django_workable_position', 'shortcode',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=25),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Position.job_shortcode'
        db.add_column('django_workable_position', 'job_shortcode',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=25),
                      keep_default=False)

        # Deleting field 'Position.shortcode'
        db.delete_column('django_workable_position', 'shortcode')


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
            'job_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'shortcode': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['django_workable']