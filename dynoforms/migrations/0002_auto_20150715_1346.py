# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynoforms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schema',
            old_name='created_by',
            new_name='owner',
        ),
    ]
