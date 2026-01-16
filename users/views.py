from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from users.forms import *


def register(request):
    if request.method == 'POST':
        form = PerfilCreateForm(request.POST) # request.FILES, contiene los archivos media, agregar solo si pusimos avatar como requisito en el registro
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('perfil_detail') # Redirigir a la página principal u otra página después del registro
    else:
        form = PerfilCreateForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_detail(request):
    return render(request, 'users/profile_detail.html', {'user': request.user})


@login_required         # class ProfileChange(login_required)
def profile_change(request):
    if request.method == 'POST':
        form = PerfilChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil_detail') # Redirigir a la página de detalles del perfil después de guardar los cambios
    else:
        form = PerfilChangeForm(instance=request.user)
    return render(request, 'users/profile_change.html', {'form': form})


