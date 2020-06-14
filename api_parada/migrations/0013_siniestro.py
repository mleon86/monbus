# Generated by Django 3.0.1 on 2020-04-30 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0001_initial'),
        ('api_parada', '0012_auto_20200428_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siniestro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time_solic', models.DateTimeField()),
                ('estado_solicitud', models.CharField(choices=[('I', 'INACTIVO'), ('A', 'ACTIVO')], default='I', max_length=10)),
                ('parada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.Parada')),
            ],
            options={
                'verbose_name': 'SiniestroParada',
                'verbose_name_plural': 'Siniestros',
                'ordering': ['time_solic'],
            },
        ),
    ]