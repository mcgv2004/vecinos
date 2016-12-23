from django.db import models
import datetime
from datetime import date, timedelta


class Calle(models.Model):
	calle = models.CharField(max_length=20)

class Casa(models.Model):
	numero = models.IntegerField()
	calle = models.ForeignKey(Calle)


class Vecino(models.Model):
	nombre = models.CharField(max_length=20)
	casa = models.ForeignKey(Casa)
	telefono = models.IntegerField()

