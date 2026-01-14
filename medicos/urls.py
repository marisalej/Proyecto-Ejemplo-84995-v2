from django.urls import path
from medicos.views import *

urlpatterns = [
   path("medicos/", MedicoListView.as_view(), name="medico_list"),
   path("medicos/crear/", MedicoCreateView.as_view(), name="medico_create"),
   path("medicos/<slug:code>/", MedicoDetailView.as_view(), name="medico_detail"),
   path("medicos/<slug:code>/editar/", MedicoUpdateView.as_view(), name="medico_update"),
   path("medicos/<int:pk>/eliminar/", MedicoDeleteView.as_view(), name="medico_delete"),
]