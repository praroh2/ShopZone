# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('customer_name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=20)),
                ('purchase_history', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'Shipping'), (3, 'Delivered'), (4, 'Returned')])),
                ('status_change_time', models.DateTimeField(verbose_name='Status Change Time')),
                ('customer', models.ForeignKey(to='store.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('clearance_time', models.DateTimeField()),
                ('amount', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('product_name', models.CharField(max_length=15)),
                ('price', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('review', models.CharField(max_length=50)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3)),
                ('product', models.ForeignKey(to='store.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('seller_name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('payment_due', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SellerReview',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('review', models.CharField(max_length=50)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3)),
                ('seller', models.ForeignKey(to='store.Seller')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(to='store.Seller'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='seller',
            field=models.ForeignKey(to='store.Seller'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(to='store.Product'),
            preserve_default=True,
        ),
    ]
