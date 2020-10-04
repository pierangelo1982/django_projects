# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galleria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, verbose_name=b'Titolo del Progetto:')),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                ('didascalia', models.TextField(null=True, blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '500x480', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                (b'slider', image_cropping.fields.ImageRatioField(b'image', '870x480', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='slider')),
                (b'thumb', image_cropping.fields.ImageRatioField(b'image', '132x94', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='thumb')),
                (b'croppinguno', image_cropping.fields.ImageRatioField(b'image', '1140x487', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppinguno')),
                (b'croppingdue', image_cropping.fields.ImageRatioField(b'image', '198x132', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingdue')),
                (b'croppingtre', image_cropping.fields.ImageRatioField(b'image', '1199x674', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingtre')),
                (b'croppingquattro', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Design Miniatura')),
                (b'croppingcinque', image_cropping.fields.ImageRatioField(b'image', '1200x800', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Design HD')),
                (b'croppingsei', image_cropping.fields.ImageRatioField(b'image', '1200x1125', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'News')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Galleria',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Immagini',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, verbose_name=b'Titolo del Progetto:')),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                ('didascalia', models.TextField(null=True, blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '500x480', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                (b'slider', image_cropping.fields.ImageRatioField(b'image', '870x480', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='slider')),
                (b'thumb', image_cropping.fields.ImageRatioField(b'image', '132x94', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='thumb')),
                (b'croppinguno', image_cropping.fields.ImageRatioField(b'image', '1140x487', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppinguno')),
                (b'croppingdue', image_cropping.fields.ImageRatioField(b'image', '198x132', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingdue')),
                (b'croppingtre', image_cropping.fields.ImageRatioField(b'image', '1199x674', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingtre')),
                (b'croppingquattro', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Design Miniatura')),
                (b'croppingcinque', image_cropping.fields.ImageRatioField(b'image', '1200x800', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Design HD')),
                (b'croppingsei', image_cropping.fields.ImageRatioField(b'image', '1200x1125', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'News')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Galleria Immagini',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, null=True, verbose_name=b'Titolo:', blank=True)),
                ('titolo_menu', models.CharField(max_length=100, null=True, verbose_name=b'Titolo Menu:', blank=True)),
                ('body', models.TextField(null=True, verbose_name=b'Descrizione', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                (b'miniatura', image_cropping.fields.ImageRatioField(b'image', '500x281', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='miniatura')),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '1200x675', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('galleria', models.ManyToManyField(to='sito.Galleria', null=True, verbose_name=b'Seleziona Immagini Galleria', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='immagini',
            name='categoria',
            field=models.ForeignKey(blank=True, to='sito.Post', null=True),
            preserve_default=True,
        ),
    ]
