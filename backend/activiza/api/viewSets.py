#Python/Django
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

#Models
from activiza.models import Ejercicio, Rutina

#Serializers
from activiza.api.serializers import EjercicioSerializer, RutinaSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer
    permission_classes = [IsAuthenticated]

class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer
    permission_classes = [IsAuthenticated]