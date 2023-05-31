from django.urls import path,include
from .forms import urls as forms_urls
from .api import urls as api_urls

urlpatterns = [
    
    #rutas para las vistas de todos los cruds
    path('forms/',include(forms_urls)),
    #rutas para la api
    path('api/',include(api_urls)),

]