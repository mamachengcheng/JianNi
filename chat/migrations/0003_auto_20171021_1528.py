# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-21 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20171021_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]