# Generated by Django 3.0.1 on 2020-03-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_bus', '0003_auto_20200318_0103'),
        ('api_parada', '0008_auto_20200320_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicasientoconsulta',
            name='viaje_inicio',
        ),
        migrations.AddField(
            model_name='solicasientoconsulta',
            name='viajes_inicios',
            field=models.ManyToManyField(to='api_bus.Viaje_Incio'),
        ),
    ]
