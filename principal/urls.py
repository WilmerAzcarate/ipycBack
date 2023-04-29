from django.contrib import admin
from django.urls import path,include
from principal.views import *

urlpatterns = [
    path('pais/', ListadoPais.as_view(template_name = "pais/tables.html"), name='leerPais')
]