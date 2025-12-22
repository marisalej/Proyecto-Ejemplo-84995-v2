from django.urls import path
from hospital.views import *


urlpatterns = [
    path("home", home, name="home"),
    path("lista_departamentos", listar_departamentos, name="departament_list"),
]
