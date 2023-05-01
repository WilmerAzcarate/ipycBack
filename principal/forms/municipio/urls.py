from django.urls import path
from .controller import *


urlpatterns = [
    
    path('', ListadoMuni.as_view(template_name = "municipio/index.html"), name='tablaMuni'),
    path('detalle/<int:pk>', MuniDetalle.as_view(template_name = "municipio/detalle.html"), name='detalleMuni'),
    path('editar/<int:pk>', MuniActualizar.as_view(template_name = "municipio/actualizar.html"), name='actualizarMuni'),   
    path('crear', MuniCrear.as_view(template_name = "municipio/crear.html"), name='crearMuni'),
    path('eliminar/<int:pk>', MuniEliminar.as_view(), name='municipio/eliminar.html')

]