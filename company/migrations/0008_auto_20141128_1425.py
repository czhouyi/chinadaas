# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_share'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='person',
        ),
        migrations.DeleteModel(
            name='Share',
        ),
    ]
