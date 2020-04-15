# Generated by Django 3.0.1 on 2020-03-20 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_bus', '0003_auto_20200318_0103'),
        ('api_parada', '0007_auto_20200319_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicasientoconsulta',
            name='viajes_inicios',
        ),
        migrations.AddField(
            model_name='solicasientoconsulta',
            name='viaje_inicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api_bus.Viaje_Incio'),
            preserve_default=False,
        ),
    ]
