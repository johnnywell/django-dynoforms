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
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', postgres.fields.JSONField(decode_kwargs={'parse_float': decimal.Decimal}, verbose_name='data', encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, blank=True)),
                ('deleted', models.BooleanField(default=False, verbose_name='deleted', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='A name to identify the schema', max_length=30, verbose_name='name')),
                ('fields', postgres.fields.JSONField(verbose_name='fields', encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='schema',
            field=models.ForeignKey(to='dynoforms.Schema'),
        ),
    ]
