from django.contrib.gis.db import models
from carga.models import Itinerario, Chofer, RaspberryBus

ESTADOS_VIAJE=(('T1','Tramo1'),('T2',"Tramo2"),('I','Intermedio'))

# Create your models here.

class Viaje_Incio(models.Model):
	id = models.AutoField(primary_key = True)#identificador de viaje proveido por el servidor al raspberry
	itinerario_id = models.ForeignKey(Itinerario, on_delete = models.CASCADE)
	chofer_id = models.OneToOneField(Chofer, on_delete = models.CASCADE)
	raspberry_id = models.OneToOneField(RaspberryBus, on_delete = models.CASCADE)
	time_rasp_logueo = models.DateTimeField(auto_now_add = False) #tiempo que provee el raspberry al momento de crearse en el bus
	time_created_logueo = models.DateTimeField(auto_now_add = True)#tiempo en el que se guarda en la base de datos

	class Meta:
		verbose_name = 'Viaje_Incio'
		verbose_name_plural = 'Viajes_Inicios'
		ordering = ['time_rasp_logueo']

	def __str__(self):
		return str(self.id)


class Bus_Datos(models.Model):
	id = models.AutoField(primary_key = True)
	viaje_inicio = models.ForeignKey(Viaje_Incio, related_name = 'viaje_inicio', on_delete = models.CASCADE)#identificador de viaje proveido por el servidor al raspberry

	time_rasp = models.DateTimeField(auto_now_add = False) #tiempo que provee el raspberry
	time_created = models.DateTimeField(auto_now_add = True)#tiempo en el que se guarda en la base de datos
	location_bus = models.PointField()#locacion del bus

	siniestro_bus = models.BooleanField(default = False)#boton de siniestro en el bus
	sensor_asiento = models.BooleanField(default = False)#sensor del asiento para personas con discapacidad
	estado_viaje = models.CharField(max_length=10, choices=ESTADOS_VIAJE, default='PY')#identificador de viaje proveido por el servidor al raspberry
	

	class Meta:
		verbose_name = 'Bus_Dato'
		verbose_name_plural = 'Bus_Datos'
		ordering = ['id']

	def __str__(self):
		return str(self.id)



#agregar asiento especial, siniestro