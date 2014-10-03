# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20140924_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='bank_balance',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
