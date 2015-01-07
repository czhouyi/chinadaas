# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0002_auto_20150107_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='desc',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='table',
            name='desc',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tablecat',
            name='desc',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
