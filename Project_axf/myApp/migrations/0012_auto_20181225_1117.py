# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-25 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_auto_20181225_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='money',
            field=models.FloatField(default=0),
        ),
    ]
