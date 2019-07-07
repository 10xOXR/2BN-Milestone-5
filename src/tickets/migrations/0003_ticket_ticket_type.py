# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-07 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20190707_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('1', 'Bug Report'), ('2', 'Feature Request')], max_length=1, null=True),
        ),
    ]
