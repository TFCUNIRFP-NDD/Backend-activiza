from rest_framework import serializers
from django.contrib.auth.models import User

#Modelos
from activiza.models import Ejercicio, Rutina

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'

class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = ('id', 'nombre', 'tipo', 'descripcion', 'ejercicios', 'media')
        depth = 1
        
class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user
    
    class Meta:
        model = User
        fields = ( "id", "username", "password", )