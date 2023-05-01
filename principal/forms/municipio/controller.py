#Librerias del crud
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

#importo el modelo de la base de datos models.py
from principal.models import *

#Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


#vista municipios
#configuracion para ver la lista de municipios
class ListadoMuni(ListView):
    model = Municipio

#configuracion para crear un municipio
class MuniCrear(SuccessMessageMixin, CreateView):
    model = Municipio
    form = Municipio
    fields = "__all__"
    success_message ='Municipio creado correctamente'
     
    def get_success_url(self):        
        return reverse('tablaPais')

#vista para ver un municipio en particular
class MuniDetalle (DetailView):
    model = Municipio

#vista para actualizar un municipio
class  MuniActualizar(SuccessMessageMixin,UpdateView):
    model =  Municipio
    form = Municipio
    fields = "__all__" 
    success_message = 'Municipio Actualizado Correctamente !'

    def get_success_url(self):               
        return reverse('tablaPais')


#configuracion para eliminar un municipio
class MuniEliminar(SuccessMessageMixin, DeleteView): 
    model = Municipio 
    form = Municipio
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Municipio Eliminado Correctamente !' 