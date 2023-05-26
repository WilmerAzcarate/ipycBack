from django.urls import path,include
from .pais import urls as pais_urls
from .departamento import urls as dep_urls
from .municipio import urls as muni_urls

urlpatterns = [
    
    #rutas para la tabla pais
    path('pais/',include(pais_urls)),
    #rutas para la tabla departamento
    path('departamento/',include(dep_urls)),     
    #rutas para la tabla municipio
    path('municipio/',include(muni_urls)) 
    
]