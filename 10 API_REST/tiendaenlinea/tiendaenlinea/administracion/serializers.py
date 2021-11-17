from rest_framework import serializers

from tiendaenlinea.administracion.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre','precio','descripcion',)
