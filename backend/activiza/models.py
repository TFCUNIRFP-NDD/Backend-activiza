from django.contrib.auth.models import User
from django.db import models

#Opciones de campos
genero_choice = (("H", "Hombre"), ("M", "Mujer"))
objetivo_choice = (("GRASA", "Perder grasa"), ("MUSCULO", "Ganar musculo"))
lugar_choice = (("C", "Casa"), ("G", "Gimnasio"))

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
        verbose_name_plural = "Entrenadores"
    
class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    ejercicios = models.ManyToManyField(Ejercicio)
    duracion = models.IntegerField(blank=True, null=True)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, blank=True, null=True)
    media = models.CharField(max_length=1000, blank=True)
    genero = models.CharField(max_length=1, choices=genero_choice)
    objetivo = models.CharField(max_length=7, choices=objetivo_choice)
    lugar_entrenamiento = models.CharField(max_length=1, choices=lugar_choice)
    
    def __str__(self):
        return str(self.nombre)    

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    altura = models.FloatField(max_length=5)
    peso = models.FloatField(max_length=5)
    genero = models.CharField(max_length=1, choices=genero_choice)
    objetivo = models.CharField(max_length=7, choices=objetivo_choice)
    lugar_entrenamiento = models.CharField(max_length=1, choices=lugar_choice)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return str(self.user.username)    
    
class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=1000)
    media = models.CharField(max_length=1000, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return str(self.titulo)  
    
    class Meta:
        verbose_name_plural = "Publicaciones"
