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