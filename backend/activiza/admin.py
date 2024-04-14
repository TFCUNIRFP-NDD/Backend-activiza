from django.contrib import admin
from activiza import models

#Modules
admin.site.register(models.Ejercicio)
admin.site.register(models.Rutina)
admin.site.register(models.Cliente)
admin.site.register(models.Entrenador)
admin.site.register(models.Publicacion)

