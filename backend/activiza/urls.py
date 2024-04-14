from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as auth

from . import views
from activiza.api import viewSets

#API - Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'ejercicio', viewSets.EjercicioViewSet)
router.register(r'rutina', viewSets.RutinaViewSet)

urlpatterns = [
    path("carga_inicial/", views.carga_inicial, name="carga_inicial"),
    path("test/", views.test, name="test"),
    path("api/rutinas", views.rutinas, name="rutinas"),
    path('api/', include(router.urls)),
    path('api-token-auth/', auth.obtain_auth_token),
]