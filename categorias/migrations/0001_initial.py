# Generated by Django 4.0.4 on 2022-06-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categoria',
            },
        ),
    ]
