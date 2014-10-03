# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20140924_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='seller',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='payment_due',
        ),
    ]
