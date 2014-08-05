# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Follow'
        db.create_table(u'actstream_follow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['newtend.NewTendUser'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('actor_only', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('started', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'actstream', ['Follow'])

        # Adding unique constraint on 'Follow', fields ['user', 'content_type', 'object_id']
        db.create_unique(u'actstream_follow', ['user_id', 'content_type_id', 'object_id'])

        # Adding model 'Action'
        db.create_table(u'actstream_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actor_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='actor', to=orm['contenttypes.ContentType'])),
            ('actor_object_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verb', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('target_content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='target', null=True, to=orm['contenttypes.ContentType'])),
            ('target_object_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('action_object_content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='action_object', null=True, to=orm['contenttypes.ContentType'])),
            ('action_object_object_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('data', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'actstream', ['Action'])


    def backwards(self, orm):
        # Removing unique constraint on 'Follow', fields ['user', 'content_type', 'object_id']
        db.delete_unique(u'actstream_follow', ['user_id', 'content_type_id', 'object_id'])

        # Deleting model 'Follow'
        db.delete_table(u'actstream_follow')

        # Deleting model 'Action'
        db.delete_table(u'actstream_action')


    models = {
        u'actstream.action': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'Action'},
            'action_object_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'action_object'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'action_object_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'actor_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actor'", 'to': u"orm['contenttypes.ContentType']"}),
            'actor_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'data': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'target_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'target'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'target_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'verb': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'actstream.follow': {
            'Meta': {'unique_together': "(('user', 'content_type', 'object_id'),)", 'object_name': 'Follow'},
            'actor_only': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'started': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['newtend.NewTendUser']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'newtend.category': {
            'Meta': {'object_name': 'Category', 'db_table': "'categories'"},
            'can_subscribe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'categories'", 'symmetrical': 'False', 'to': "orm['newtend.KeyWord']"}),
            'lang': ('django.db.models.fields.CharField', [], {'default': "'ru'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['newtend.Category']", 'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.SmallIntegerField', [], {}),
            'url_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'newtend.city': {
            'Meta': {'object_name': 'City', 'db_table': "'cities'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'default': "'ru'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'phone_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cities'", 'to': "orm['newtend.Region']"})
        },
        'newtend.company': {
            'Meta': {'ordering': "['created']", 'object_name': 'Company', 'db_table': "'companies'"},
            'activated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bank_account_num': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'bank_info': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'default': "u''", 'related_name': "'city'", 'null': 'True', 'blank': 'True', 'to': "orm['newtend.City']"}),
            'comments': ('django.db.models.fields.TextField', [], {'default': "u''", 'null': 'True', 'blank': 'True'}),
            'corporate_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'companies'", 'null': 'True', 'to': "orm['newtend.CorporateGroup']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'default_delivery_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_delivery_address'", 'null': 'True', 'to': "orm['newtend.DeliveryAddresses']"}),
            'egrpo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'fax': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inn': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'moderated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'nds': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent_company': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_companies'", 'null': 'True', 'to': "orm['newtend.Company']"}),
            'phones': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['newtend.Phone']", 'symmetrical': 'False'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '2', 'decimal_places': '1'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'region'", 'null': 'True', 'to': "orm['newtend.Region']"}),
            'registrator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'my_company'", 'to': "orm['newtend.NewTendUser']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'site': ('django.db.models.fields.URLField', [], {'default': "u''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sphere': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['newtend.Sphere']", 'symmetrical': 'False'}),
            'subscribe': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['newtend.Category']", 'null': 'True', 'blank': 'True'}),
            'subscribe_cities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['newtend.City']", 'null': 'True', 'blank': 'True'}),
            'subscribe_regions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['newtend.Region']", 'null': 'True', 'blank': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'companies'", 'blank': 'True', 'through': "orm['newtend.UserCompanySettings']", 'to': "orm['newtend.NewTendUser']"}),
            'verified_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verified_phone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verified_post_address': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verified_tax': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'newtend.corporategroup': {
            'Meta': {'object_name': 'CorporateGroup', 'db_table': "'company_groups'"},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'admin_group'", 'to': "orm['newtend.NewTendUser']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['newtend.NewTendUser']"}),
            'friend_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['newtend.CorporateGroup']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100'})
        },
        'newtend.deliveryaddresses': {
            'Meta': {'ordering': "['address']", 'object_name': 'DeliveryAddresses', 'db_table': "'delivery_addresses'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'city'", 'null': 'True', 'blank': 'True', 'to': "orm['newtend.City']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'delivery_addresses'", 'to': "orm['newtend.Company']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'newtend.keyword': {
            'Meta': {'object_name': 'KeyWord', 'db_table': "'keywords'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'newtend.newtenduser': {
            'Meta': {'object_name': 'NewTendUser', 'db_table': "'users'", 'index_together': "[['first_name', 'last_name']]"},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owner'", 'null': 'True', 'to': "orm['newtend.Company']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'default_role': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_operator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'last_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'new_offers_period': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'new_tenders_period': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'news_period': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'patronymics': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50'}),
            'phones': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['newtend.Phone']", 'symmetrical': 'False'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'receive_new_offers': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'receive_new_tenders': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'receive_news': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'reg_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'Europe/Kiev'", 'max_length': '50'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'newtend.phone': {
            'Meta': {'object_name': 'Phone', 'db_table': "'phones'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('newtend.lib.phone_field.modelfields.PhoneNumberField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'newtend.region': {
            'Meta': {'object_name': 'Region', 'db_table': "'regions'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'default': "'ru'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'newtend.sphere': {
            'Meta': {'object_name': 'Sphere', 'db_table': "'spheras'"},
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'parent sphere'", 'null': 'True', 'blank': 'True', 'to': "orm['newtend.Sphere']"})
        },
        'newtend.usercompanysettings': {
            'Meta': {'unique_together': "(['company', 'user'],)", 'object_name': 'UserCompanySettings', 'db_table': "'user_company_settings'"},
            'can_participate_in_tenders': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_see_bids': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_see_tenders': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users_settings'", 'to': "orm['newtend.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'companies_settings'", 'to': "orm['newtend.NewTendUser']"})
        }
    }

    complete_apps = ['actstream']