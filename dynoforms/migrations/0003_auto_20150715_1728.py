# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.serializers.json
import decimal
import postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynoforms', '0002_auto_20150715_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', postgres.fields.JSONField(decode_kwargs={'parse_float': decimal.Decimal}, verbose_name='data', encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, blank=True)),
                ('deleted', models.BooleanField(default=False, verbose_name='deleted', editable=False)),
                ('schema', models.ForeignKey(to='dynoforms.Schema')),
            ],
        ),
        migrations.RemoveField(
            model_name='data',
            name='schema',
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
