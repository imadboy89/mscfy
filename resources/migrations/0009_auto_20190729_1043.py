# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-07-29 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_auto_20190726_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.Album'),
        ),
    ]
