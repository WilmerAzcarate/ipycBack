#Librerias del crud
from django.shortcuts import render

# Create your views here.

#pantalla principal
def Home(request):
    return render(request,'index.html')