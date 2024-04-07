from django.contrib.auth.models import User
from django.db import models

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    repeticiones = models.IntegerField()
    duracion = models.IntegerField()
    descanso = models.IntegerField()
    media = models.CharField(max_length=1000, blank=True)
    
    def __str__(self):
        return str(self.nombre)
    
class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=1000)
    descripcion = models.CharField(max_length=1000)
    ejercicios = models.ManyToManyField(Ejercicio)
    
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    altura = models.FloatField(max_length=5)
    peso = models.FloatField(max_length=5)
