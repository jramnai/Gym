# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-10 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
