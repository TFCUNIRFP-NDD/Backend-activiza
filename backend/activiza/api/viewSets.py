#Python/Django
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from django.http.response import JsonResponse

#Models
from activiza.models import Ejercicio, Publicacion, Entrenador, Cliente

#Serializers
from activiza.api.serializers import EjercicioSerializer, UserSerializer, PublicacionSerializer, ClienteSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']
    
    def create(self, request):
        user = User.objects.create_user(
            username = request.data['username'],
            password = request.data['password'],
            email = request.data['username']
        )
        
        token = Token.objects.create(user = user)
                
        return JsonResponse({"token": f"{token}"}, safe=False, status=status.HTTP_201_CREATED)
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']
    
    def create(self, request):
        serializer = ClienteSerializer(data=request.data)
                
        if serializer.is_valid():            
            #Se crea el cliente y se devuelve
            cliente = Cliente.objects.create(user = request.user, altura = request.data["altura"], peso = request.data["peso"], genero = request.data["genero"], objetivo = request.data["objetivo"], lugar_entrenamiento = request.data["lugar_entrenamiento"], entrenador = Entrenador.objects.get(pk=1))
            cliente_serializer = ClienteSerializer(cliente)
            
            return JsonResponse(cliente_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    
    def create(self, request):
        serializer = PublicacionSerializer(data=request.data)
                
        if serializer.is_valid():
            #Identificamos al entrenador logueado 
            try:
                Entrenador.objects.get(user=request.user)
            except Exception:
                return HttpResponse("No tienes permisos para crear rutinas.")
            
            #Se crea la rutina y se devuelve
            publicacion = Publicacion.objects.create(titulo = request.data["titulo"], mensaje = request.data["mensaje"], autor = request.user)
            publicacion_serializer = PublicacionSerializer(publicacion)
            
            return JsonResponse(publicacion_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)