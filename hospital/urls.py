from django.urls import path
from hospital.views import *


urlpatterns = [
    path("", home, name="home"),
    path("lista_departamentos", listar_departamentos, name="listar_departamentos"),
    path("crear_depto", crear_departamento, name="crear_departamento"),
    path("ver_departamento/<int:pk>/", ver_departamento, name="ver_departamento"),
]
