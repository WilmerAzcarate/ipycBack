#Librerias del crud
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

#importo el modelo de la base de datos models.py
from principal.models import Municipio as table

#Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


#vistas
class ListadoMuni(ListView):
    model = table

class MuniCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message ='Municipio creado correctamente'
     
    def get_success_url(self):        
        return reverse('tablaMuni')

class MuniDetalle (DetailView):
    model = table

class  MuniActualizar(SuccessMessageMixin,UpdateView):
    model =  table
    form = table
    fields = "__all__" 
    success_message = 'Municipio Actualizado Correctamente !'

    def get_success_url(self):               
        return reverse('tablaMuni')

class MuniEliminar(SuccessMessageMixin, DeleteView): 
    model = table 
    form = table
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Municipio Eliminado Correctamente !' 