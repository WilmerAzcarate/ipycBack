from django.urls import path
from .controller import *


urlpatterns = [
    
    #rutas para la tabla pais
    path('', ListadoDep.as_view(template_name = "pais/index.html"), name='tablaDep'),
    path('detalle/<int:pk>',DepDetalle.as_view(template_name = "pais/detalle.html"), name='detalleDep'),
    path('editar/<int:pk>', DepActualizar.as_view(template_name = "pais/actualizar.html"), name='actualizarDep'),   
    path('crear', DepCrear.as_view(template_name = "pais/crear.html"), name='crearDep'),
    path('eliminar/<int:pk>', DepEliminar.as_view(), name='pais/eliminar.html')

]