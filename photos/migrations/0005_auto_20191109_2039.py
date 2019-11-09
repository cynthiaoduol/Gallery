# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-09 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='photos.Category'),
        ),
        migrations.AddField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='photos.Location'),
        ),
    ]