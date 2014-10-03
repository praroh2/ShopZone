# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20140925_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('review', models.CharField(max_length=50)),
                ('rating', models.IntegerField(default=3, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('time_stamp', models.DateTimeField(verbose_name='Date-time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
