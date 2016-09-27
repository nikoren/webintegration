from django.db import models

# Create your models here.

from django.db import models
from django.contrib.postgres.fields import JSONField
import json


name, order, queue, user_facing = 0, 1, 2, 3
chain_to_steps = {

    #      name,                      order, queue, user_facing
    'products': [
        ('sku_upc_prd_map',              1,  False, True,),
        ('stores',                       2,  False, True),
        ('tax',                          3,  False, True),
        ('categories',                   4,  False, True),
        ('store_products',               5,  False,  True),
        ('product_locations',            6,  False,  True),
        ('categories_stores_map',        7,  False, False),
        ('product_images',               8,  False,  True),
        ('product_details',              9,  False,  True),
        ('product_nutritions',          10,  False,  True),
        ('map_product_details',         12,  False, False),
        ('products_cache',              13,  False, False),
        ('index_products',              14,  True,  False)
    ],

    #      name,                      order, queue, user_facing
    'pricing': [
        ('base_price_delete',            1,   False, True),
        ('base_price_delta',             2,   False, True),
        ('base_price_full',              3,   False, True),
        ('sale_price_delete',            4,   False, True),
        ('sale_price_delta',             5,   False, True),
        ('sale_price_full',              6,   False, True),
        ('bobbarker',                    7,   False, False),
        ('store_products_cache',         8,   False, False),
    ],

    #      name,                      order, queue, user_facing
    'tlog': [
        ('tlog_headers',                 1,  False, True),
        ('tlog_lineitems',               2,  False, True),
        ('consume_staged_tlog',          3,  False, False)
    ],

    #      name,                      order, queue, user_facing
    'flyer': [
        ('flyer_delete',                 1,  True,  True),
        ('flyer',                        2,  True,  True),
    ]
}
step_to_schema = {}


class Chain(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    name = models.CharField(max_length=100, blank=False)
    type = models.CharField(max_length=100,choices=[(chain_name, chain_name) for chain_name in chain_to_steps.keys()])
    owner = models.ForeignKey('auth.User', related_name='chains', related_query_name='chain')

    def save(self, *args, **kwargs):
        """
        Control how instances of the model saved
        """

        super(Chain, self).save(*args, **kwargs)

    def __str__(self):
        return '{} - {} chain object'.format(self.name,self.type)

class Step(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    chain = models.ForeignKey('Chain', on_delete=models.CASCADE, related_name='steps', related_query_name='step')
    step_type = models.CharField(
        choices=[(step[name], step[name])
                 for steps_list in chain_to_steps.values()
                 for step in steps_list
                 if step[user_facing]],
        blank=False,
        max_length=100)
    integration_data = JSONField()


    def save(self, *args, **kwargs):
        """
        Control how instances of the model saved
        """

        super(Step, self).save(*args, **kwargs)

    class Meta:
        ordering = ['step_type']







