from django.contrib.auth.models import User
from django.db import models

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    repeticiones = models.IntegerField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    descanso = models.IntegerField()
    media = models.CharField(max_length=1000, blank=True)
    
    def __str__(self):
        return str(self.nombre)
    
class Entrenador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        verbose_name = "Entrenadore"
    
class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    ejercicios = models.ManyToManyField(Ejercicio)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, blank=True, null=True)
    media = models.CharField(max_length=1000, blank=True)
    
    def __str__(self):
        return str(self.nombre)    

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    altura = models.FloatField(max_length=5)
    peso = models.FloatField(max_length=5)
    objetivo = models.CharField(max_length=1000)
    genero = models.CharField(max_length=50)
    lugar_entrenamiento = models.CharField(max_length=50)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return str(self.user.username)    
    
class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=1000)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return str(self.titulo)  
    
    class Meta:
        verbose_name = "Publicacione"