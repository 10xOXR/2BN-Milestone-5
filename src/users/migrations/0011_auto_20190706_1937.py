# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-06 19:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190706_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
    ]
