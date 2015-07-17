# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import postgres.fields
import decimal
import django.core.serializers.json
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('_updated', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('_deleted', models.BooleanField(default=False, verbose_name='deleted', editable=False)),
                ('data', postgres.fields.JSONField(decode_kwargs={'parse_float': decimal.Decimal}, verbose_name='data', encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, blank=True)),
                ('_owner', models.ForeignKey(help_text=b'Who created it', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('_updated', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('_deleted', models.BooleanField(default=False, verbose_name='deleted', editable=False)),
                ('name', models.CharField(help_text='A name to identify the schema', max_length=30, verbose_name='name')),
                ('description', models.TextField(help_text='A description to guide the form usage', verbose_name='description', blank=True)),
                ('fields', postgres.fields.JSONField(verbose_name='fields', encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
                ('_owner', models.ForeignKey(help_text=b'Who created it', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='schema',
            field=models.ForeignKey(to='dynoforms.Schema'),
        ),
    ]
