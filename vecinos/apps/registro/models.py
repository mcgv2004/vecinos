from django.db import models
import datetime
from datetime import date, timedelta


class Calle(models.Model):
	calle = models.CharField(max_length=20)
	def __str__(self):
		return unicode(self.calle)

class Casa(models.Model):
	numero = models.IntegerField()
	calle = models.ForeignKey(Calle)
	def __str__(self):
		return unicode(self.numero)  + self.calle

class Vecino(models.Model):
	nombre = models.CharField(max_length=20)
	casa = models.ForeignKey(Casa)
	telefono = models.IntegerField()

	def __str__(self):
		return unicode(self.nombre + self.casa + self.telefono)