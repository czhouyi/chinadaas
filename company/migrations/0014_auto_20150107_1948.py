# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_person_passwd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('status', models.CharField(default=b'0', max_length=2, choices=[(b'0', b'\xe6\x99\xae\xe9\x80\x9a'), (b'1', b'\xe5\x80\x9f\xe5\x87\xba'), (b'2', b'\xe9\x81\x97\xe5\xa4\xb1')])),
                ('desc', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='cat',
            field=models.ForeignKey(to='company.BookCat'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(to='company.Person', blank=True),
            preserve_default=True,
        ),
    ]
