# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20141215_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='MacAddr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wire_ip', models.CharField(max_length=15, blank=True)),
                ('wire_mac', models.CharField(max_length=17, blank=True)),
                ('wire_less_ip', models.CharField(max_length=15, blank=True)),
                ('wire_less_mac', models.CharField(max_length=17, blank=True)),
                ('has_pro_pm', models.BooleanField(default=False)),
                ('remark', models.CharField(max_length=100, blank=True)),
                ('person', models.ForeignKey(to='company.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
