from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as auth
from activiza.customAuthToken import CustomAuthToken
from . import views
from activiza.api import viewSets

#API viewsets autogenerados
router = routers.DefaultRouter()
router.register(r'ejercicio', viewSets.EjercicioViewSet)
router.register(r'user', viewSets.UserViewSet)
router.register(r'cliente', viewSets.ClienteViewSet)
router.register(r'publicaciones', viewSets.PublicacionViewSet)

urlpatterns = [
    path("carga_inicial/", views.carga_inicial, name="carga_inicial"),
    path("test/", views.test, name="test"),
    path("api/rutina/", views.rutina, name="rutina"),
    path('api/rutina/<int:pk>', views.rutina_detalle, name="rutina_detalle"),
    path('api/', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view()),
]