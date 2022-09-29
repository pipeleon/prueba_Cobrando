from django.db import models


"""Clase de la Tabla Departamento"""
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    presupuesto = models.FloatField()

"""Clase de la Tabla Empleado con relacion 1 a muchos con la tabla Departamento"""
class Empleado(models.Model):
    nif = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100, blank=True)
    codigo_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
