# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_customer_bank_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='bank_balance',
            new_name='store_credit',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.IntegerField(default=1, choices=[(1, 'Paid from store credit'), (2, 'Cash on delivery')]),
            preserve_default=True,
        ),
    ]
