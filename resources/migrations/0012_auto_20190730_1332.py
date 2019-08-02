# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-07-30 13:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0011_auto_20190730_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
