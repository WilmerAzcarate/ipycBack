from django.urls import path
from .controller import *


urlpatterns = [
    
    path('', ListadoDep.as_view(template_name = "departamento/index.html"), name='tablaDep'),
    path('detalle/<int:pk>',DepDetalle.as_view(template_name = "departamento/detalle.html"), name='detalleDep'),
    path('editar/<int:pk>', DepActualizar.as_view(template_name = "departamento/actualizar.html"), name='actualizarDep'),   
    path('crear', DepCrear.as_view(template_name = "departamento/crear.html"), name='crearDep'),
    path('eliminar/<int:pk>', DepEliminar.as_view(), name='departamento/eliminar.html')

]