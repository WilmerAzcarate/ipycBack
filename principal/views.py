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
        return reverse('tablaPais')

#vista para ver un pais en particular
class PaisDetalle (DetailView):
    model = Pais

#vista para actualizar un pais
class  PaisActualizar(SuccessMessageMixin,UpdateView):
    model =  Pais
    form = Pais
    fields = "__all__" 
    success_message = 'Pais Actualizado Correctamente !'

    def get_success_url(self):               
        return reverse('tablaPais')


#configuracion para eliminar un pais
class PaisEliminar(SuccessMessageMixin, DeleteView): 
    model = Pais 
    form = Pais
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Pais Eliminado Correctamente !' 
        
#vista departamentos
#configuracion para ver la lista de departamentos
class ListadoDep(ListView):
    model = Departamento

#configuracion para crear un departamento
class DepCrear(SuccessMessageMixin, CreateView):
    model = Departamento
    form = Departamento
    fields = "__all__"
    success_message ='Departamento creado correctamente'
     
    def get_success_url(self):        
        return reverse('tablaDep')

#vista para ver un departamento en particular
class DepDetalle (DetailView):
    model = Departamento

#vista para actualizar un departamento
class  DepActualizar(SuccessMessageMixin,UpdateView):
    model =  Departamento
    form = Departamento
    fields = "__all__" 
    success_message = 'Departamento Actualizado Correctamente !'

    def get_success_url(self):               
        return reverse('tablaDep') 


#configuracion para eliminar un departamento
class DepEliminar(SuccessMessageMixin, DeleteView): 
    model = Departamento 
    form = Departamento
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Departamento Eliminado Correctamente !'