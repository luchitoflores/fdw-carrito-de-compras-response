#encoding:utf-8
from django.db import models
from django.template import defaultfilters
from django.contrib.auth.models import User


class Familia(models.Model):
    nombre = models.CharField(max_length=99, unique=True)
    slug = models.SlugField(max_length=99, unique=True)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre)
        super(Familia, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre


class Fabricante(models.Model):
    nombre = models.CharField(max_length=99, unique=True)

    def __unicode__(self):
        return self.nombre


class Recambio(models.Model):
    familia = models.ForeignKey(Familia)
    fabricante = models.ForeignKey(Fabricante)
    nombre = models.CharField(max_length=99)
    precio = models.FloatField()
    slug = models.SlugField(max_length=99, unique=True)

    def save(self, *args, **kwargs):
        super(Recambio, self).save(*args, **kwargs)
        self.slug = defaultfilters.slugify('%s-%i' % (self.nombre, self.id))
        super(Recambio, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre


class CarritoDeCompra(models.Model):
    user = models.ForeignKey(User)
    recambio = models.ForeignKey(Recambio)
    unidades = models.PositiveSmallIntegerField()
    precio = models.FloatField()

    class Meta:
        verbose_name_plural = 'Carritos de compra'

    def __unicode__(self):
        return unicode(self.user)
