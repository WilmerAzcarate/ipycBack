#Librerias del crud
from django.shortcuts import render

# Create your views here.

#pantalla principal
def Home(request):
    return render(request,'index.html')

#pantalla de login
def Login(request):
    return render(request,'login.html')

#pantalla de registro
def Register(request):
    return render(request,'register.html')