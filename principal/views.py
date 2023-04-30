#Librerias del crud
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

#importo el modelo de la base de datos models.py
from principal.models import *

#Habilitamos el uso de mensajes de django
from django.contrib import messages

#Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

#Habilitamos los formularios en django
from django import forms


# Create your views here.

#pantalla principal
def Home(request):
    return render(request,'index.html')

#vista paises
#configuracion para ver la lista de paises
class ListadoPais(ListView):
    model = Pais

#configuracion para crear un pais
class PaisCrear(SuccessMessageMixin, CreateView):
    model = Pais
    form = Pais
    fields = "__all__"
    success_message ='Pais creado correctamente'
     
    def get_success_url(self):        
        return reverse('tablaPais') # Redireccionamos a la vista principal 'leer'

#vista para ver un pais en particular
class PaisDetalle (DetailView):
    model = Pais

#vista para actualizar un pais
class  PaisActualizar(SuccessMessageMixin,UpdateView):
    model =  Pais
    form = Pais
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Pais Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('tablaPais') # Redireccionamos a la vista principal 'leer'


#configuracion para eliminar un pais
class PaisEliminar(SuccessMessageMixin, DeleteView): 
    model = Pais 
    form = Pais
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Pais Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
