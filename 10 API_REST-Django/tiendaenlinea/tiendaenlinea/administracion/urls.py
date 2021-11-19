from django.urls import path, include

from rest_framework import routers

from tiendaenlinea.administracion.views import lista_productos, producto_detalle,lista_clientes

router = routers.DefaultRouter()
urlpatterns = [
    path('producto/', include(router.urls)),
    path('productos/', lista_productos),
    path('productos/<int:pk>', producto_detalle),
    path('clientes/',lista_clientes)
]
