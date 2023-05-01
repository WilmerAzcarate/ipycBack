from principal.models import Pais as table
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

#responses
def listar_paises(request):
    paises = table.objects.all()
    data = list(paises.values())
    return JsonResponse(data, safe=False)

def obtener_pais(request, pk):
    pais = get_object_or_404(table, pk=pk)
    data = {
        'id': pais.pk,
        'nombre': pais.nombre,
        'codigo': pais.codigo,
    }
    return JsonResponse(data)

def crear_pais(request):
    nombre = request.POST.get('nombre')
    codigo = request.POST.get('codigo')
    pais = table(nombre=nombre,codigo=codigo)
    pais.save()
    return JsonResponse({'success': True})

def actualizar_pais(request, pk):
    pais = get_object_or_404(table, pk=pk)
    pais.nombre = request.POST.get('nombre')
    pais.codigo = request.POST.get('codigo')
    pais.save()
    return JsonResponse({'success': True})

def eliminar_pais(request, pk):
    pais = get_object_or_404(table, pk=pk)
    pais.delete()
    return JsonResponse({'success': True})
