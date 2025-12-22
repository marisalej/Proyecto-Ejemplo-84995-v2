from django.shortcuts import render
from hospital.models import DepartamentoMedico

def home(request):
    return render(request, "hospital/index.html")


def listar_departamentos(request):
    departamentos_query = DepartamentoMedico.objects.all() #list(QuerySet[Depto, ...., Depto, ....]) 
    contexto = {
        "departamentos": departamentos_query
    }
    return render(request, "hospital/departamentos_medicos.html", contexto)


