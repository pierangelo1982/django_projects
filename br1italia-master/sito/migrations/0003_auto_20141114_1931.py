# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0002_auto_20141027_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immagini',
            name=b'slider',
            field=image_cropping.fields.ImageRatioField(b'image', '830x530', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='slider'),
            preserve_default=True,
        ),
    ]
