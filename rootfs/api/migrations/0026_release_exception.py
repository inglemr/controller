# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_app_procfile_structure'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='exception',
            field=models.TextField(blank=True, null=True),
        ),
    ]
