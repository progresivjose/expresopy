# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'New.created'
        db.add_column(u'news_new', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 5, 24, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'New.modified'
        db.add_column(u'news_new', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 24, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'New.created'
        db.delete_column(u'news_new', 'created')

        # Deleting field 'New.modified'
        db.delete_column(u'news_new', 'modified')


    models = {
        u'news.new': {
            'Meta': {'object_name': 'New'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['news']