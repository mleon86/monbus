# Generated by Django 3.0.1 on 2020-02-06 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_bus', '0006_auto_20200206_0109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bus_datos',
            options={'ordering': ['id'], 'verbose_name': 'Bus_Dato', 'verbose_name_plural': 'Bus_Datos'},
        ),
    ]
