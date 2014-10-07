# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PieceCategory.background_gradient_top'
        db.add_column(u'project_piececategory', 'background_gradient_top',
                      self.gf('django.db.models.fields.CharField')(default='#4267a7', max_length=7),
                      keep_default=False)

        # Adding field 'PieceCategory.background_gradient_bottom'
        db.add_column(u'project_piececategory', 'background_gradient_bottom',
                      self.gf('django.db.models.fields.CharField')(default='#3c607c', max_length=7),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PieceCategory.background_gradient_top'
        db.delete_column(u'project_piececategory', 'background_gradient_top')

        # Deleting field 'PieceCategory.background_gradient_bottom'
        db.delete_column(u'project_piececategory', 'background_gradient_bottom')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'project.piece': {
            'Meta': {'object_name': 'Piece', '_ormbases': ['shop.Product']},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pieces'", 'null': 'True', 'to': u"orm['project.PieceCategory']"}),
            'hero_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'sold': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'project.piececategory': {
            'Meta': {'object_name': 'PieceCategory'},
            'background_gradient_bottom': ('django.db.models.fields.CharField', [], {'default': "'#3c607c'", 'max_length': '7'}),
            'background_gradient_top': ('django.db.models.fields.CharField', [], {'default': "'#4267a7'", 'max_length': '7'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_shop.product_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        }
    }

    complete_apps = ['project']