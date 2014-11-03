# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_customer_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=1000)),
                ('product', models.ForeignKey(to='store.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
