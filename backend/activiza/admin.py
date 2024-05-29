from django.contrib import admin
from activiza import models

#Modules
admin.site.register(models.Ejercicio)
admin.site.register(models.Rutina)
admin.site.register(models.Cliente)
admin.site.register(models.Entrenador)
admin.site.register(models.Publicacion)

admin.site.site_header = "Panel de control Activiza - Gimnasio Peperoni"
admin.site.index_title = "Panel de control Activiza"
