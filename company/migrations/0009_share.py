# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20141128_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('attach', models.FileField(upload_to=b'../static/company/share/uploads')),
                ('desc', models.CharField(max_length=100)),
                ('person', models.ForeignKey(to='company.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
