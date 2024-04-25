#Python/Django
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from django.http.response import JsonResponse

#Models
from activiza.models import Ejercicio, Publicacion, Entrenador

#Serializers
from activiza.api.serializers import EjercicioSerializer, UserSerializer, PublicacionSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer
    #permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]
    http_method_names = ['post']
    
class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    #permission_classes = [IsAuthenticated]
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
            publicacion = Publicacion.objects.create(titulo = request.data["titulo"], mensaje = request.data["mensaje"], autor = logged_user)
            publicacion_serializer = PublicacionSerializer(publicacion)
            
            return JsonResponse(publicacion_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)