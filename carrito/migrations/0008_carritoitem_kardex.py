# Generated by Django 4.0.4 on 2022-07-07 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_alter_kardex_producto'),
        ('carrito', '0007_remove_carritoitem_kardex'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritoitem',
            name='kardex',
            field=models.ManyToManyField(blank=True, to='productos.kardex'),
        ),
    ]
