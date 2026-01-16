from django.shortcuts import render, redirect, get_object_or_404
from hospital.models import DepartamentoMedico
from hospital.forms import DepartamentoMedicoForm, DepartamentoMedicoUpdateForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "hospital/index.html")

@login_required
def listar_departamentos(request):
    nombre = request.GET.get("nombre")
    departamentos_query = DepartamentoMedico.objects.all() #list(QuerySet[Depto, ...., Depto, ....]) 
    if nombre: # si nombre NO ES None / '' / etc
        departamentos_query = DepartamentoMedico.objects.filter(
            nombre__icontains=nombre
        )
    contexto = {
        "departamentos": departamentos_query
    }
    return render(request, "hospital/departamentos_medicos.html", contexto)

#GET = pedir infor
#POST - crear / editar info
#PUT - actualizar info
#DELETE - eliminar info

@login_required
def crear_departamento(request):
    if request.method == "POST":
        form = DepartamentoMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_departamentos")
    else:
        form = DepartamentoMedicoForm()
    
    return render(request, 'hospital/crear_departamento.html', {'form': form})

@login_required
def ver_departamento(request, pk):
    departamento = get_object_or_404(DepartamentoMedico, pk=pk)
    context = {
        "departamento": departamento
    }
    
    return render(request, 'hospital/ver_departamento.html', context)


@login_required
def actualizar_departamento(request, nro_departamento):
    departamento = get_object_or_404(DepartamentoMedico, nro_departamento=nro_departamento)

    if request.method == "POST":
        form = DepartamentoMedicoUpdateForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect("ver_departamento", pk=departamento.pk)
    else:
        form = DepartamentoMedicoUpdateForm(instance=departamento)
    
    return render(request, 'hospital/crear_departamento.html', {
        "form": form, 
        "departamento": departamento,
        "update": True
    })

@login_required
def eliminar_departamento(request, nro_departamento):
    departamento = get_object_or_404(DepartamentoMedico, nro_departamento=nro_departamento)
    departamento.delete()
    return redirect("listar_departamentos")
    