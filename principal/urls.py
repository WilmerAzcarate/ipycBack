from django.contrib import admin
from django.urls import path
from principal.views import *

urlpatterns = [
    
    #rutas para la tabla pais
    path('pais/', ListadoPais.as_view(template_name = "pais/index.html"), name='tablaPais'),
    path('pais/detalle/<int:pk>', PaisDetalle.as_view(template_name = "pais/detalle.html"), name='detallePais'),
    path('pais/editar/<int:pk>', PaisActualizar.as_view(template_name = "pais/actualizar.html"), name='actualizarPais'),   
    path('pais/crear', PaisCrear.as_view(template_name = "pais/crear.html"), name='crearPais'),
    path('pais/eliminar/<int:pk>', PaisEliminar.as_view(), name='pais/eliminar.html'),
    #rutas para la tabla departamento
    path('departamento/', ListadoDep.as_view(template_name = "departamento/index.html"), name='tablaDep'),
    path('departamento/detalle/<int:pk>', DepDetalle.as_view(template_name = "departamento/detalle.html"), name='detalleDep'),
    path('departamento/editar/<int:pk>', DepActualizar.as_view(template_name = "departamento/actualizar.html"), name='actualizarDep'), 
    path('departamento/crear', DepCrear.as_view(template_name = "departamento/crear.html"), name='crearDep'),
    path('departamento/eliminar/<int:pk>', DepEliminar.as_view(), name='departamento/eliminar.html')      

]