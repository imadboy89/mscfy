# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-07-22 11:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20190722_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img_link', models.CharField(default='https://cdn1.vectorstock.com/images/1000x1000/37/05/5053705.jpg?download=1', max_length=250)),
                ('date_release', models.DateField(blank=True, null=True, verbose_name='date released ')),
                ('date_addded', models.DateTimeField(auto_now_add=True, null=True, verbose_name='added to platform')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='added to platform')),
                ('artists', models.ManyToManyField(to='resources.Artists')),
            ],
        ),
        migrations.AddField(
            model_name='songs',
            name='img_link',
            field=models.CharField(default='https://cdn1.vectorstock.com/images/1000x1000/37/05/5053705.jpg?download=1', max_length=250),
        ),
        migrations.AddField(
            model_name='songs',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resources.Albums'),
            preserve_default=False,
        ),
    ]
