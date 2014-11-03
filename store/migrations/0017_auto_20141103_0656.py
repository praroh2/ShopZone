# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='link',
            field=models.CharField(max_length=2000),
            preserve_default=True,
        ),
    ]
