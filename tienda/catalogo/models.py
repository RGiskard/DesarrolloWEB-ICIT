from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombreArticulo = models.CharField(max_length=100,default="",null=False)
    precioArticulo = models.FloatField(default=1,null=False)
    descripcionArticulo = models.TextField(default="",null=True)

class Area(models.Model):
    codigoArea = models.CharField(max_length=7,default="",unique=True)
    nombreArea = models.CharField(max_length=100,default="",null=False)

class Vendedor(models.Model):
    dniVendedor = models.CharField(max_length=8,null=False,unique=True)
    nombreVendedor = models.CharField(max_length=255,null=False)
    comisionVendedor = models.FloatField(null=False)