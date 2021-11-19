from django.contrib import admin

# Register your models here.
from tiendaenlinea.administracion.models import Producto,Cliente

admin.site.register(Producto)
admin.site.register(Cliente)
