from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as auth
from activiza.api.customAuthToken import CustomAuthToken
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
    path("api/rutina/", views.get_rutinas, name="rutina"),
    path('api/rutina/<int:pk>', views.get_rutina_detalle, name="rutina_detalle"),
    path('api/', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('generate-qr-code/', views.get_qr_code, name='generate-qr-code')
]