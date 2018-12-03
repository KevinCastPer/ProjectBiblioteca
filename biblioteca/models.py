# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return "%s %s"%(self.nombre, self.apellidos)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to='portadas')

    def __str__(self):
        return self.titulo
