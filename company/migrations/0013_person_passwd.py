# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_auto_20150105_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='passwd',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
