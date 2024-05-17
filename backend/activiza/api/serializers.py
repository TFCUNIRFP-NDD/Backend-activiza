from rest_framework import serializers
from django.contrib.auth.models import User

#Modelos
from activiza.models import Ejercicio, Rutina, Publicacion, Cliente

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'

class RutinaSerializer(serializers.ModelSerializer):
    entrenador = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='user__username'
     )
    
    class Meta:
        model = Rutina
        fields = ('id', 'nombre', 'duracion', 'genero', 'objetivo', 'lugar_entrenamiento', 'entrenador', 'descripcion', 'ejercicios', 'media')
        depth = 1
        
class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        
        user.email = validated_data['username']

        return user
    
    class Meta:
        model = User
        fields = ( "id", "username", "password")

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ("altura", "peso", "objetivo", "genero", "lugar_entrenamiento")

class PublicacionSerializer(serializers.ModelSerializer):
    autor = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
     )
    
    class Meta:
        model = Publicacion
        fields = '__all__'
        
