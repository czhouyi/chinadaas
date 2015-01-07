# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.CharField(default=1, max_length=2, choices=[(0, b'\xe7\xa6\xbb\xe8\x81\x8c'), (1, b'\xe5\x9c\xa8\xe8\x81\x8c')]),
            preserve_default=True,
        ),
    ]
