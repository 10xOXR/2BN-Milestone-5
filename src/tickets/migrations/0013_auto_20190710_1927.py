# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-10 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_auto_20190710_1856'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
