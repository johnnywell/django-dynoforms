# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-06 20:56
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='deleted')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, verbose_name='data')),
                ('owner', models.ForeignKey(help_text='Who created it', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='deleted')),
                ('name', models.CharField(help_text='A name to identify the schema', max_length=30, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='A description to guide the form usage', verbose_name='description')),
                ('fields', django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder, verbose_name='fields')),
                ('owner', models.ForeignKey(help_text='Who created it', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynoforms.Schema'),
        ),
    ]
