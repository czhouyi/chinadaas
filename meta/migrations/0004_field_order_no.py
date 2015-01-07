# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0003_auto_20150107_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='order_no',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
