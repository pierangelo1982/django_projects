# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kml', '0003_auto_20160309_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='colore',
            field=models.CharField(blank=True, help_text='For more information about KML color: http://www.netdelight.be/kml/index.php', max_length=255, null=True, verbose_name='Colore Riferimento Percorso'),
        ),
    ]
