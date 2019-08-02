# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-07-22 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_auto_20190719_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='link',
        ),
        migrations.AddField(
            model_name='artists',
            name='img_link',
            field=models.CharField(default='https://cdn1.vectorstock.com/images/1000x1000/37/05/5053705.jpg?download=1', max_length=250),
        ),
        migrations.AddField(
            model_name='songs',
            name='link_mp3',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='extra link'),
        ),
        migrations.AlterField(
            model_name='artists',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
