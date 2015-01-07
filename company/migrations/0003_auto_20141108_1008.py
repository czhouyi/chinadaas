# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_person_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(default=b'1', max_length=2, choices=[(b'0', b'\xe7\xa6\xbb\xe8\x81\x8c'), (b'1', b'\xe5\x9c\xa8\xe8\x81\x8c')]),
            preserve_default=True,
        ),
    ]
