from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    precio = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
