# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 03:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('products', 'products'), ('pricing', 'pricing'), ('flyer', 'flyer'), ('tlog', 'tlog')], max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chains', related_query_name='chain', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('step_type', models.CharField(choices=[('sku_upc_prd_map', 'sku_upc_prd_map'), ('stores', 'stores'), ('tax', 'tax'), ('categories', 'categories'), ('store_products', 'store_products'), ('product_locations', 'product_locations'), ('product_images', 'product_images'), ('product_details', 'product_details'), ('product_nutritions', 'product_nutritions'), ('base_price_delete', 'base_price_delete'), ('base_price_delta', 'base_price_delta'), ('base_price_full', 'base_price_full'), ('sale_price_delete', 'sale_price_delete'), ('sale_price_delta', 'sale_price_delta'), ('sale_price_full', 'sale_price_full'), ('flyer_delete', 'flyer_delete'), ('flyer', 'flyer'), ('tlog_headers', 'tlog_headers'), ('tlog_lineitems', 'tlog_lineitems')], max_length=100)),
                ('integration_data', models.TextField()),
                ('chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', related_query_name='step', to='web_integration_app.Chain')),
            ],
            options={
                'ordering': ['step_type'],
            },
        ),
    ]
