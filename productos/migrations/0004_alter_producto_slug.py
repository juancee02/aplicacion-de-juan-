# Generated by Django 4.0.4 on 2022-06-23 00:16

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_producto_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='nombre'),
        ),
    ]
