# Generated by Django 4.0.6 on 2022-08-02 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_contactos_celular_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideas',
            name='Apellido',
            field=models.TextField(default='', max_length=340),
        ),
        migrations.AddField(
            model_name='ideas',
            name='Correo',
            field=models.TextField(default='', max_length=340),
        ),
        migrations.AddField(
            model_name='ideas',
            name='Nombre',
            field=models.TextField(default='', max_length=340),
        ),
        migrations.AddField(
            model_name='ideas',
            name='Telefono',
            field=models.TextField(default='', max_length=11),
        ),
    ]
