from pickletools import decimalnl_short
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
#from regiones.models import *
from clientes.models import *

import uuid
from pathlib import Path
import os

# Create your models here.

class Vacante(models.Model):
    SEXO = (
        ('Ambos', 'Ambos'),
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),)
    
    formacion = (
        ('*', '*'),
        ('Primaria','Primaria'),
        ('Bachiller','Bachiller'),
        ('Técnica Laboral','Técnica Laboral'),
        ('Técnica Profesional','Técnica Profesional'),
        ('Tecnológica','Tecnológica'),
        ('Universitaria','Universitaria'),)

    especializacion = (
        ('NO','NO'),
        ('Especialización','Especialización'),
        ('Maestría','Maestría'),
        ('Doctorado','Doctorado'),
        )
    PRESENCIAL = (
        ('Presencial', 'Presencial'),
        ('Virtual', 'Virtual'),
        ('Presencial y Virtual', 'Presencial y Virtual'),)

    ESTADO = (
        ('Abierta', 'Abierta'),
        ('Cerrada', 'Cerrada'),
        ('Suspendida', 'Suspendida'),)
    
    CONTRATO = (
        ('Prestacion Servicios', 'Prestacion Servicios'),
        ('Obra o Labor', 'Obra o Labor'),
        ('Termino Fijo', 'Termino Fijo'),
        ('Indefinido', 'Indefinido'),)
   

    id = models.AutoField(primary_key=True)
    Cliente = models.ForeignKey(Empresa, null=True, on_delete=models.CASCADE)
    contacto = models.ForeignKey(Contactos, null=True, on_delete=models.CASCADE)
    ClienteFinal = models.CharField(max_length=200)
    CargoSolicitado =  models.CharField(max_length=200)
    cantidad = models.PositiveIntegerField(default = '1')
    Sector =	models.ForeignKey(SectorEconomico, null=True, on_delete=models.CASCADE)
    Depto =	models.ForeignKey(departamentos, null=True, on_delete=models.CASCADE)
    Ciudad = models.ForeignKey(ciudades, null=True, on_delete=models.CASCADE)
    Genero = models.CharField(max_length=200, null=True, choices=SEXO)
    EdadMinima = models.PositiveIntegerField(default=18, validators=[MinValueValidator(16), MaxValueValidator(60)])
    EdadMaxima = models.PositiveIntegerField(default=45, validators=[MinValueValidator(18), MaxValueValidator(60)])
    Educacion = models.CharField(max_length = 50, choices = formacion, default = 'Bachiller')
    AreaFormacion = models.CharField(max_length=200)
    Especializacion = models.CharField(max_length = 50, choices = especializacion, default = 'NO')
    Certificados = models.CharField(max_length=200, default = 'NO')
    Pase = models.CharField(max_length=200, default = 'NO')
    MesesExperiencia = models.PositiveIntegerField(default = '1')
    ConocimientoEspecifico = models.TextField()
    FuncionesCargo= models.TextField(null=True, blank=True, default = 'Encargado de ')
    Horario = models.CharField(max_length=200, default = 'Lunes-Sábado')
    Presencialidad = models.CharField(max_length = 50, choices = PRESENCIAL, default = 'Presencial')
    SitioLabor = models.CharField(max_length=200)
    Salario = models.DecimalField(max_digits = 9, decimal_places = 0, default = '0')
    Bonos = models.CharField(max_length=200)
    SalarioEmocional = models.CharField(max_length=200)
    TipoContrato = models.CharField(max_length = 50, choices = CONTRATO, default = 'Obra o Labor')
    NotaEspecial = models.TextField()
    Entrevista = models.CharField(max_length = 50, choices = PRESENCIAL, default = 'Presencial')
    direccionEntrevista = models.CharField(max_length=200)
    FechaInicio = models.DateField(auto_now_add=True)
    FechaFin = models.DateField(auto_now_add=True)
    EstadoDDR = models.CharField(max_length = 50, choices = ESTADO, default = 'Abierta', verbose_name="Estado")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ("Cliente",)        
    def __str__(self):
        return str(self.Cliente)


class Categoria(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class ArchivoVacante(models.Model):
    id = models.AutoField(primary_key=True)
    vacante = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)    
    archivo = models.FileField(upload_to='imagenes/', null=True, blank=True)
    formularios = models.CharField(max_length=250, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ("id",)        
    def __str__(self):
        return str(self.vacante)


    def save(self, *args, **kwargs):    #https://scottbarnham.com/blog/category/django/page/2/index.html
        for field in self._meta.fields:
            if field.name == 'archivo':
                path = str(self.vacante) 
                #Curriculum_Hvfield.upload_to = "profile_pics{0}/{1}".format(6, path) 
                field.upload_to = "imagenes/vacantes/{0}".format(path)  
        super(ArchivoVacante, self).save()

