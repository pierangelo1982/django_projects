# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kml', '0008_remove_path_mappa_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='mappa',
            field=models.FileField(blank=True, null=True, upload_to='uploads/kml/'),
        ),
    ]
