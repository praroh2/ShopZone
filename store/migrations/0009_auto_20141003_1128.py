# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_storereview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, 'New'), (2, 'Shipping'), (3, 'Delivered'), (4, 'Returned'), (5, 'Cancelled')]),
        ),
    ]
