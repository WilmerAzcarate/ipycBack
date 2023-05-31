from django.urls import path
from .views import *


urlpatterns = [
    
    path('', ListadoTIdentificacion.as_view(template_name = "TIdentificacion/index.html"), name='tablaTIdentificacion'),
    path('detalle/<int:pk>', TIdentificacionDetalle.as_view(template_name = "TIdentificacion/detalle.html"), name='detalleTIdentificacion'),
    path('editar/<int:pk>', TIdentificacionActualizar.as_view(template_name = "TIdentificacion/actualizar.html"), name='actualizarTIdentificacion'),   
    path('crear', TIdentificacionCrear.as_view(template_name = "TIdentificacion/crear.html"), name='crearTIdentificacion'),
    path('eliminar/<int:pk>', TIdentificacionEliminar.as_view(), name='TIdentificacion/eliminar.html')

]