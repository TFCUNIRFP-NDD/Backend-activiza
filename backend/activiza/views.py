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
    
    return HttpResponse("Carga de datos inicial completada.")

@login_required
@api_view(['GET', 'POST'])
def rutinas(request):
    if request.method == 'GET':
        rutina = Rutina.objects.all()
        

        
        rutina_serializer = RutinaSerializer(rutina, many=True)
        return JsonResponse(rutina_serializer.data, safe=False)