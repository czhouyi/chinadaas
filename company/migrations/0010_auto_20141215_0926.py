# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_share'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='desc',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='qq',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='share',
            name='attach',
            field=models.FileField(upload_to=b'../static/company/share/uploads', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='share',
            name='created',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='share',
            name='desc',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
