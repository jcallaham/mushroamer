# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0005_auto_20170726_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='odor',
            field=models.CharField(default='', max_length=40, verbose_name='Odor'),
        ),
    ]
