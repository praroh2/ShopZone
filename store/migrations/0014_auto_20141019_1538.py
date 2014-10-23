# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20141019_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('category_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('customer_name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=20)),
                ('purchase_history', models.IntegerField(default=0)),
                ('store_credit', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('payment_type', models.IntegerField(default=1, choices=[(1, 'Paid from store credit'), (2, 'Cash on delivery')])),
                ('status', models.IntegerField(default=1, choices=[(1, 'New'), (2, 'Shipping'), (3, 'Delivered'), (4, 'Returned'), (5, 'Cancelled')])),
                ('status_change_time', models.DateTimeField(verbose_name='Status Change Time')),
                ('customer', models.ForeignKey(to='store.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('product_name', models.CharField(max_length=30)),
                ('number_sold', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('review', models.CharField(max_length=50)),
                ('rating', models.IntegerField(default=3, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('sentiment', models.IntegerField(default=0)),
                ('time_stamp', models.DateTimeField(verbose_name='Date-time')),
                ('product', models.ForeignKey(to='store.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('seller_name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SellerReview',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('review', models.CharField(max_length=50)),
                ('rating', models.IntegerField(default=3, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('sentiment', models.IntegerField(default=0)),
                ('time_stamp', models.DateTimeField(verbose_name='Date-time')),
                ('seller', models.ForeignKey(to='store.Seller')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoreReview',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('review', models.CharField(max_length=50)),
                ('rating', models.IntegerField(default=3, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('sentiment', models.IntegerField(default=0)),
                ('time_stamp', models.DateTimeField(verbose_name='Date-time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('sub_category_name', models.CharField(max_length=20)),
                ('category', models.ForeignKey(to='store.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='store.SubCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
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
