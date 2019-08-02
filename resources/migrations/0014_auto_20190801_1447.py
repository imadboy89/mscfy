# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-08-01 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0013_auto_20190730_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='last_name',
        ),
        migrations.AddField(
            model_name='artist',
            name='country',
            field=models.CharField(default='fname', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='date_release',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='date released '),
        ),
        migrations.AlterField(
            model_name='artist',
            name='neck_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
