# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-20 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190706_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='https://2bn-unicorn-attractor.s3.amazonaws.com/media/prof_img/default.jpg', null=True, upload_to='prof_img'),
        ),
    ]
