# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20141005_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number_sold',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
