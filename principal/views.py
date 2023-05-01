#Librerias del crud
from django.shortcuts import render

#importo el modelo de la base de datos models.py
from principal.models import *


# Create your views here.

#pantalla principal
def Home(request):
    return render(request,'index.html')