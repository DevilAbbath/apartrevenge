from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

def index(request):
    return render(request, 'aptrent/base.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después de registrarse
            return redirect('base')  # Redirige a la página principal o cualquier otra
    else:
        form = UserCreationForm()
    return render(request, 'aptrent/registro.html', {'form': form})

def custom_logout(request):
    # Cerrar sesión
    logout(request)
    # Redirigir a una página de confirmación
    return render(request, 'registration/logout.html')
