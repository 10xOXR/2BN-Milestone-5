# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-29 18:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0016_auto_20190720_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Badge',
                'verbose_name_plural': 'Badges',
            },
        ),
        migrations.CreateModel(
            name='BadgeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge_type', models.CharField(max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Badge Type',
                'verbose_name_plural': 'Badge Types',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='user_bugs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_features',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='badges',
            name='badge_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.BadgeType'),
        ),
        migrations.AddField(
            model_name='badges',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]