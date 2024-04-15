from rest_framework import serializers

#Modelos
from activiza.models import Ejercicio, Rutina

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'

class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = ('nombre', 'tipo', 'descripcion', 'ejercicios')
        depth = 1