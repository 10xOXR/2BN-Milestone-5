# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-29 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20190729_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgetype',
            name='badge_type',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
