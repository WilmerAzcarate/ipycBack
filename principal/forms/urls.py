from django.urls import path,include
from .pais import urls as pais_urls
from .departamento import urls as dep_urls

urlpatterns = [
    
    #rutas para la tabla pais
    path('pais/',include(pais_urls)),
    #rutas para la tabla departamento
    path('departamento/',include(dep_urls))     

]