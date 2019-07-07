# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-07 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20190707_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('To-Do (Not Started)', 'To-Do (Not Started)'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='In Progress', max_length=20),
        ),
    ]
