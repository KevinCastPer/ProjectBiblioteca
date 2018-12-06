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
        verbose_name_plural = "Editores"


    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    email = models.EmailField(blank=True, null=True, verbose_name="e-mail")
    # email = models.EmailField('e-mail', blank=True, null=True)
    ultimo_acceso = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Autores"

    def __str__(self):
        return "%s %s"%(self.nombre, self.apellidos)

class ManejadorLibros(models.Manager):
    def contar_titulos(self, keyword):
        return self.filter(titulo__icontains=keyword).count()

# Primero, definimos una subclase para el Manager.
class DahlLibroManager(models.Manager):
    def get_query_set(self):
        return super(DahlLibroManager, self).get_query_set().filter(autores='Roald Dahl')

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to='portadas')
    num_paginas = models.IntegerField(blank=True, null=True)
    objects = ManejadorLibros() # El manager predeterminado.
    dahl_objects = DahlLibroManager() # El manager "Dahl" especial.


    def __str__(self):
        return self.titulo



# Otro ejemplo como funciona con manejador con filter separado de sexo para coger la lista de genero diferente.
# class ManejadorMujeres(models.Manager):
#     def get_query_set(self):
#         return super(ManejadorMujeres, self).get_query_set().filter(sexo='M')
#
# class ManejadorHombres(models.Manager):
#     def get_query_set(self):
#         return super(ManejadorHombres, self).get_query_set().filter(sexo='H')
#
# class Persona(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     sexo = models.CharField(max_length=1, choices=(('M', 'Mujer'), ('H', 'Hombre')))
#     gente = models.Manager() # EL manejador predeterminado.
#     hombre = ManejadorHombres()# Devuelve solo hombres.
#     mujer = ManejadorMujeres()# Devuelve solo mujeres.
