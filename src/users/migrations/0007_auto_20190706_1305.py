# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-06 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190706_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
