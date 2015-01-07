# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_link_ping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='ping',
        ),
    ]
