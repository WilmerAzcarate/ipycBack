#Librerias del crud
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

#importo el modelo de la base de datos models.py
from principal.models import *

#Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

#Habilitamos los formularios en django
from django import forms

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