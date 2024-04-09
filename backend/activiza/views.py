from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.contrib.auth.decorators import login_required

#App
from activiza.models import Ejercicio, Rutina
from activiza.api.serializers import EjercicioSerializer, RutinaSerializer

def carga_inicial(request):
    try:
        #Gestor
        user = User.objects.create_user("admin", "admin@admin.com", "admin")
        user.is_staff=True
        user.is_superuser=True
        user.save()
        
        #Entrenador
        user = User.objects.create_user("entrenador", "entrenador@entrenador.com", "entrenador")
        user.is_staff=True
        user.save()
        
        #Cliente
        user = User.objects.create_user("cliente", "cliente@cliente.com", "cliente")
        user.peso = 95.5
        user.altura = 180
        user.save()
    except Exception:
        print("Usuarios ya existentes.")
        
    entrenador = User.objects.get(username="entrenador")
    
    #Rutinas
    for x in range(0,5):
        rutina = Rutina.objects.create(nombre = f"NombreRutina{x}", tipo = f"TipoRutina{x}", descripcion = f"Descripcion{x}", entrenador = entrenador)    
    
        #Ejercicios
        for y in range(0,10):
            ejercicio = Ejercicio.objects.create(nombre = f"NombreEjercicio{x}{y}", descripcion = f"DescripcionEjercicio{x}{y}", repeticiones = 2, descanso = 1)
            
            rutina.ejercicios.add(ejercicio)

    return HttpResponse("Carga de datos inicial completada.")

@api_view(['GET', 'POST'])
def rutinas(request):
    if request.method == 'GET':
        rutina = Rutina.objects.all()
        rutina_serializer = RutinaSerializer(rutina, many=True)
        return JsonResponse(rutina_serializer.data, safe=False)