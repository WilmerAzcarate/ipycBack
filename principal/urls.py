from django.urls import path,include
from .forms import urls as forms_urls

urlpatterns = [
    
    #rutas para la tabla pais
    path('forms/',include(forms_urls))      

]