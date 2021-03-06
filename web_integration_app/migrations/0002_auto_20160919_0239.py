# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-19 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_integration_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chain',
            name='type',
            field=models.CharField(choices=[('products', 'products'), ('flyer', 'flyer'), ('pricing', 'pricing'), ('tlog', 'tlog')], max_length=100),
        ),
        migrations.AlterField(
            model_name='step',
            name='step_type',
            field=models.CharField(choices=[('sku_upc_prd_map', 'sku_upc_prd_map'), ('stores', 'stores'), ('tax', 'tax'), ('categories', 'categories'), ('store_products', 'store_products'), ('product_locations', 'product_locations'), ('product_images', 'product_images'), ('product_details', 'product_details'), ('product_nutritions', 'product_nutritions'), ('flyer_delete', 'flyer_delete'), ('flyer', 'flyer'), ('base_price_delete', 'base_price_delete'), ('base_price_delta', 'base_price_delta'), ('base_price_full', 'base_price_full'), ('sale_price_delete', 'sale_price_delete'), ('sale_price_delta', 'sale_price_delta'), ('sale_price_full', 'sale_price_full'), ('tlog_headers', 'tlog_headers'), ('tlog_lineitems', 'tlog_lineitems')], max_length=100),
        ),
    ]
