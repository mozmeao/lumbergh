# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.name'
        db.add_column('django_workable_category', 'name',
                      self.gf('django.db.models.fields.CharField')(default='h', max_length=100),
                      keep_default=False)

        # Adding field 'Category.slug'
        db.add_column('django_workable_category', 'slug',
                      self.gf('django.db.models.fields.CharField')(default='h', unique=True, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.name'
        db.delete_column('django_workable_category', 'name')

        # Deleting field 'Category.slug'
        db.delete_column('django_workable_category', 'slug')


    models = {
        'django_workable.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
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