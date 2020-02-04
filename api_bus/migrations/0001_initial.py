# Generated by Django 3.0.1 on 2020-02-04 15:53

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje_Incio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time_rasp_logueo', models.DateTimeField()),
                ('time_created_logueo', models.DateTimeField(auto_now_add=True)),
                ('chofer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carga.Chofer')),
                ('itinerario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.Itinerario')),
                ('raspberry_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carga.RaspberryBus')),
            ],
            options={
                'verbose_name': 'Viaje_Incio',
                'verbose_name_plural': 'Viajes_Inicios',
                'ordering': ['time_rasp_logueo'],
            },
        ),
        migrations.CreateModel(
            name='Bus_Datos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time_rasp', models.DateTimeField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('siniestro_bus', models.BooleanField(default=False)),
                ('sensor_asiento', models.BooleanField(default=False)),
                ('estado_viaje', models.CharField(choices=[('T1', 'Tramo1'), ('T2', 'Tramo2'), ('I', 'Intermedio')], default='PY', max_length=10)),
                ('location_bus', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('viaje_inicio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_bus.Viaje_Incio')),
            ],
            options={
                'verbose_name': 'Bus_Dato',
                'verbose_name_plural': 'Bus_Datos',
                'ordering': ['viaje_inicio_id'],
            },
        ),
    ]
