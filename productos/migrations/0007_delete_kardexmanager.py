# Generated by Django 4.0.4 on 2022-07-05 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_kardexmanager_alter_kardex_kardex_categoria'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KardexManager',
        ),
    ]
