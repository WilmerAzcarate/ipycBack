from django.contrib import admin
from django.urls import path
from principal.views import *

urlpatterns = [
    
    #rutas para la tabla pais
    #ruta para ver la tabla de paises
    path('pais/', ListadoPais.as_view(template_name = "pais/index.html"), name='tablaPais'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('pais/detalle/<int:pk>', PaisDetalle.as_view(template_name = "pais/detalle.html"), name='detallePais'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('pais/editar/<int:pk>', PaisActualizar.as_view(template_name = "pais/actualizar.html"), name='actualizarPais'), 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('pais/crear', PaisCrear.as_view(template_name = "pais/crear.html"), name='crearPais'),
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('pais/eliminar/<int:pk>', PaisEliminar.as_view(), name='pais/eliminar.html')    

]