# Generated by Django 3.0.1 on 2019-12-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_Parada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parada', models.CharField(max_length=200)),
                ('siniestro', models.CharField(max_length=200)),
                ('prep_asiento', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Datos_Parada',
                'verbose_name_plural': 'Datos_Paradas',
                'ordering': ['parada'],
            },
        ),
    ]
