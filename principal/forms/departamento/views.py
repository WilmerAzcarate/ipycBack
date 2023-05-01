#Librerias del crud
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

#importo el modelo de la base de datos models.py
from principal.models import Departamento as table

#Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

#Habilitamos los formularios en django
from django import forms

#vistas
class ListadoDep(ListView):
    model = table

class DepCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message ='Departamento creado correctamente'
     
    def get_success_url(self):        
        return reverse('tablaDep')

class DepDetalle (DetailView):
    model = table

class  DepActualizar(SuccessMessageMixin,UpdateView):
    model =  table
    form = table
    fields = "__all__" 
    success_message = 'Departamento Actualizado Correctamente !'

    def get_success_url(self):               
        return reverse('tablaDep') 


class DepEliminar(SuccessMessageMixin, DeleteView): 
    model = table 
    form = table
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Departamento Eliminado Correctamente !'