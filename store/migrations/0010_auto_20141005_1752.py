# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20141003_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='sentiment',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productreview',
            name='time_stamp',
            field=models.DateTimeField(verbose_name='Date-time', default=datetime.date(2014, 10, 5)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sellerreview',
            name='sentiment',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sellerreview',
            name='time_stamp',
            field=models.DateTimeField(verbose_name='Date-time', default=datetime.date(2014, 10, 5)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storereview',
            name='sentiment',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
