import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import action
from .utils import generate_qr_code
from rest_framework.authtoken.models import Token

#App
from activiza.models import Ejercicio, Rutina, Publicacion, Cliente, Entrenador
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
        Entrenador.objects.create(user=user)
        
        #Cliente
        user = User.objects.create_user("cliente", "cliente@cliente.com", "cliente")
        Cliente.objects.create(user = user, peso = 95.5, altura = 180, objetivo = "perder_peso")
        
    except Exception:
        print("Usuarios ya existentes.")
        
    entrenador = Entrenador.objects.get(user=User.objects.get(username="entrenador"))
    
    #Rutinas
    for x in range(0,2):
        rutina = Rutina.objects.create(nombre = f"NombreRutina{x}", descripcion = f"Descripcion{x}", entrenador = entrenador, media= "https://i.imgur.com/Z7EHhdu.jpeg", genero = "M", objetivo = "GRASA", lugar_entrenamiento = "G")    
    
        #Ejercicios
        for y in range(0,5):
            ejercicio = Ejercicio.objects.create(nombre = f"NombreEjercicio{x}{y}", descripcion = f"DescripcionEjercicio{x}{y}", repeticiones = 2, descanso = 1, media= "https://i.imgur.com/Z7EHhdu.jpeg")
            
            rutina.ejercicios.add(ejercicio)

    return HttpResponse("Carga de datos inicial completada.")

@api_view(['GET', 'POST'])
def get_rutinas(request):
    
    if request.method == 'GET':     
        try:
            if request.GET: 
                query_dict = request.GET.dict()     

                #Obtenemos las rutinas segun los filtros, busqueda global, sin entrenador
                rutina_serializer = RutinaSerializer(Rutina.objects.filter(**query_dict), many=True)

            else:
                #Obtenemos las rutinas del entrenador asignado al cliente
                cliente = Cliente.objects.get(user = request.user)
                rutina_serializer = RutinaSerializer(Rutina.objects.filter(entrenador = cliente.entrenador), many=True)
            
            return JsonResponse(rutina_serializer.data, safe=False)
        except Exception:
            try:
                #No es cliente quien hace la petición, obtenemos las rutinas del entrenador
                entrenador = Entrenador.objects.get(user = request.user)
                rutina_serializer = RutinaSerializer(Rutina.objects.filter(entrenador = entrenador), many=True)

                return JsonResponse(rutina_serializer.data, safe=False)
            except Exception:
                return JsonResponse({"error": "El usuario no tiene rutinas asignadas."}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        #Identificamos al entrenador logueado 
        try:
            entrenador = Entrenador.objects.get(user=request.user)
        except Exception:
            return JsonResponse({"error": "No tienes permisos para crear rutinas."}, status=status.HTTP_403_FORBIDDEN)
        
        body = json.loads(request.body)
        
        #Se crea la rutina y se devuelve
        rutina = Rutina.objects.create(nombre = body["nombre"], descripcion = body["descripcion"], duracion = body["duracion"], media = body["media"], genero = body["genero"], objetivo = body["objetivo"], lugar_entrenamiento = body["lugar_entrenamiento"], entrenador = entrenador)
        rutina_serializer = RutinaSerializer(rutina)
        
        #Asociamos todos los ejercicios de la rutina
        for ejercicio in body["ejercicios"]:
            print(ejercicio)
            rutina.ejercicios.add(Ejercicio.objects.get(id = ejercicio))
        
        return JsonResponse(rutina_serializer.data, safe=False)
    
@api_view(['GET', 'PUT', 'DELETE'])
def get_rutina_detalle(request, pk):
    
    try: 
        rutina = Rutina.objects.get(pk=pk) 
    except Rutina.DoesNotExist: 
        return JsonResponse({'message': 'No existe la rutina.'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        rutina_serializer = RutinaSerializer(rutina) 
        return JsonResponse(rutina_serializer.data) 

    elif request.method == 'PUT': 
        #Identificamos al entrenador logueado 
        try:
            Entrenador.objects.get(user=request.user)
        except Exception:
            return JsonResponse({"error": "No tienes permisos para editar rutinas."}, status=status.HTTP_403_FORBIDDEN)
        
        rutina_data = JSONParser().parse(request) 
        rutina_serializer = RutinaSerializer(rutina, data=rutina_data) 
        
        if rutina_serializer.is_valid(): 
            rutina_serializer.save() 
            return JsonResponse(rutina_serializer.data) 
        return JsonResponse(rutina_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        #Identificamos al entrenador logueado 
        try:
            Entrenador.objects.get(user=request.user)
        except Exception:
            return JsonResponse({"error": "No tienes permisos para eliminar rutinas."}, status=status.HTTP_403_FORBIDDEN)
        
        rutina.delete() 
        return JsonResponse({'message': f'Rutina {pk} eliminada.'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def get_qr_code(request):
    try: 
        #Generamos el QR con los datos
        token = Token.objects.get(user = request.user)
        data_to_encode = f"Token {token.key}"  # Customize as needed
        qr_code = generate_qr_code(data_to_encode)

        #Devolvemos la imagen generada
        response = HttpResponse(content_type="image/png")
        qr_code.save(response, "PNG")
        return response
    
    except Exception: 
        return JsonResponse({'message': 'No tienes permisos para ver el QR.'}, status=status.HTTP_403_FORBIDDEN) 
    