# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_macaddr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macaddr',
            name='remark',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='macaddr',
            name='wire_ip',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='macaddr',
            name='wire_less_ip',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='macaddr',
            name='wire_less_mac',
            field=models.CharField(max_length=17, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='macaddr',
            name='wire_mac',
            field=models.CharField(max_length=17, null=True),
            preserve_default=True,
        ),
    ]
