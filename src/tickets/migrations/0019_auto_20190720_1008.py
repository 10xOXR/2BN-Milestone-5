# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-20 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0018_auto_20190720_0957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketstatus',
            options={'verbose_name': 'Ticket Status', 'verbose_name_plural': 'Ticket Status'},
        ),
    ]
