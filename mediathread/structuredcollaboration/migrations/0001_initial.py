# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CollaborationPolicyRecord'
        db.create_table('structuredcollaboration_collaborationpolicyrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('policy_name', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('structuredcollaboration', ['CollaborationPolicyRecord'])

        # Adding model 'Collaboration'
        db.create_table('structuredcollaboration_collaboration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.Group'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=None, max_length=1024, null=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default=None, max_length=50, null=True, db_index=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='collaboration_set_for_collaboration', null=True, to=orm['contenttypes.ContentType'])),
            ('object_pk', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('_policy', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['structuredcollaboration.CollaborationPolicyRecord'], null=True, blank=True)),
            ('_parent', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='children', null=True, blank=True, to=orm['structuredcollaboration.Collaboration'])),
            ('context', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='context_children', null=True, blank=True, to=orm['structuredcollaboration.Collaboration'])),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=5352)),
        ))
        db.send_create_signal('structuredcollaboration', ['Collaboration'])

        # Adding unique constraint on 'Collaboration', fields ['content_type', 'object_pk']
        db.create_unique('structuredcollaboration_collaboration', ['content_type_id', 'object_pk'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Collaboration', fields ['content_type', 'object_pk']
        db.delete_unique('structuredcollaboration_collaboration', ['content_type_id', 'object_pk'])

        # Deleting model 'CollaborationPolicyRecord'
        db.delete_table('structuredcollaboration_collaborationpolicyrecord')

        # Deleting model 'Collaboration'
        db.delete_table('structuredcollaboration_collaboration')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'structuredcollaboration.collaboration': {
            'Meta': {'ordering': "['title']", 'unique_together': "(('content_type', 'object_pk'),)", 'object_name': 'Collaboration'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '5352'}),
            '_parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'children'", 'null': 'True', 'blank': 'True', 'to': "orm['structuredcollaboration.Collaboration']"}),
            '_policy': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['structuredcollaboration.CollaborationPolicyRecord']", 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'collaboration_set_for_collaboration'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'context_children'", 'null': 'True', 'blank': 'True', 'to': "orm['structuredcollaboration.Collaboration']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_pk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'structuredcollaboration.collaborationpolicyrecord': {
            'Meta': {'object_name': 'CollaborationPolicyRecord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'policy_name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['structuredcollaboration']
