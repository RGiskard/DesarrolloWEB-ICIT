from rest_framework import serializers
from rest_framework.reverse import reverse
from tiendaenlinea.administracion.models import Producto,Cliente


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre','precio','descripcion',)

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente 
        fields=('usuario','dni',)