# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-06 13:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190706_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, max_length=2, null=True, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
    ]
