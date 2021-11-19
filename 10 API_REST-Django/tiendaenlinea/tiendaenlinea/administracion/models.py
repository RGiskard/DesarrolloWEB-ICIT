from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    precio = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

class Cliente(models.Model):
    usuario = models.CharField(max_length=20, null=False)
    dni = models.CharField(max_length=12, null=False,unique=True)

class Factura(models.Model):
    codigo_Factura = models.CharField(max_length=9,null=False,unique=True)
    fecha_venta = models.DateTimeField(null=False)
    cliente_asociado = models.ForeignKey('Cliente',on_delete=models.DO_NOTHING)
    productos = models.ManyToManyField('Producto')