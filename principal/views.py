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

#configuracion para ver la lista de paises
class ListadoPais(ListView):
    model = Pais