from django.db import models


class Calle(models.Model):
    calle = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.calle

    def get_absolute_url(self):
        return "/calle/%s/" % self.slug


class Like(models.Model):
    like = models.ForeignKey(Calle)


class Casa(models.Model):
    numero = models.IntegerField()
    calle = models.ForeignKey(Calle)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.calle.calle + " " + str(self.numero)

    def get_absolute_url(self):
        return "/casa/%s/" % self.slug


class Vecino(models.Model):
    nombre = models.CharField(max_length=20)
    casa = models.ForeignKey(Casa)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre + self.casa + self.telefono


class Prevision(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class TipoBono(models.Model):
    tipo_bono = models.CharField(max_length=50)
    prevision = models.ManyToManyField(Prevision, through='BonoPrevision')


class BonoPrevision(models.Model):
    bono = models.ForeignKey(TipoBono)
    prevision = models.ForeignKey(Prevision)

