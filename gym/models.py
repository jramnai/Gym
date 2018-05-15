# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.FileField()
    product_description = models.TextField(max_length=1000, blank=True)
    product_stock = models.PositiveIntegerField()
    product_available = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name
