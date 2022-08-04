from sre_parse import Verbose
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


#***********************regiones y Paises****************************


# Create your models here.
class paises(models.Model):
    IdPais = models.CharField(max_length=50, primary_key=True)
    pais = models.CharField(max_length=50, null=True)
    Simbol = models.CharField(max_length=50, null=True)

    class Meta:
        #verbose_name = _("Profile")
        #verbose_name_plural = _("Profiles")
        ordering = ("pais",)

    def __str__(self):
        fila=self.pais
        return fila


class departamentos(models.Model):
    IdPais =  models.ForeignKey(paises, on_delete=models.CASCADE, null=True)
    idDepto = models.CharField(primary_key=True, max_length=50 )
    Departamento = models.CharField(max_length=50, null=True)
    class Meta:
        #verbose_name = _("Profile")
        #verbose_name_plural = _("Profiles")
        ordering = ("Departamento",)
    def __str__(self):
       # fila=self.Departamento
        return self.Departamento

class ciudades(models.Model):
    IdPais =	models.ForeignKey(paises, on_delete=models.CASCADE, null=True)
    idDepto =	models.ForeignKey(departamentos, on_delete=models.CASCADE, null=True)
    idCiudad =	models.CharField(primary_key=True, max_length=50)
    Ciudad =	models.CharField(max_length=50, null=True)
    
    def __str__(self):
        fila=self.Ciudad
        return fila

# Create your models here.
class SectorEconomico(models.Model):
    id = models.AutoField(primary_key=True)
    Sector =models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "SectorEconomico"
        ordering = ("Sector",)
    def __str__(self):
        return self.Sector



class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=200)
    dv = models.CharField(max_length=10)   
    RazonSocial = models.CharField(max_length=200, null=True)
    Actividad = models.ForeignKey(SectorEconomico, null=True, on_delete=models.CASCADE, verbose_name='Actividad Economica')
    Direccion = models.CharField(max_length=200, null=True)
    Pais =	models.ForeignKey(paises, null=True, on_delete=models.CASCADE)
    Depto =	models.ForeignKey(departamentos, null=True, on_delete=models.CASCADE)
    Ciudad = models.ForeignKey(ciudades, null=True, on_delete=models.CASCADE)
    telefonos = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254, null=True, blank=True)
    web = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    logoEmpresa = models.ImageField(upload_to='imagenes/', verbose_name='logo', null=True, blank=True, default='imagenes/3.png')
    
    #esta linea sirve para borrar imagenes del directorio imagenes/
    def delete(self, using=None, keep_parents=False):
        self.logoEmpresa.storage.delete(self.logoEmpresa.name)
        super().delete()

    class Meta:
        verbose_name_plural = "Empresa"
        ordering = ("RazonSocial",)
    def __str__(self):
        return str(self.RazonSocial)
    
class Contactos(models.Model):
    id = models.AutoField(primary_key=True)
    Empresa = models.ForeignKey(Empresa, null=True, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=200, null=True)
    Cargo =	models.CharField(max_length=200, null=True)
    celular =	models.CharField(max_length=200, null=True)
    Correo =	models.EmailField(max_length = 254)   	
    Pais =	models.ForeignKey(paises, null=True, on_delete=models.CASCADE)
    Depto =	models.ForeignKey(departamentos, null=True, on_delete=models.CASCADE)
    Ciudad = models.ForeignKey(ciudades, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "Directorio"
        ordering = ("Empresa","Nombre",)
    def __str__(self):
        return self.Nombre
        #return f"{self.Empresa} |  {self.Nombre} | Cargo: {self.Cargo}"
    



