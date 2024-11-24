from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .decorators import check_user_type
from .forms import CustomUserCreationForm

# Mantenedor de otras Paginas
def index(request):
    return render(request, 'aptrent/base.html')

@login_required
@check_user_type('arrendador')
def arrendadores_view(request):
    return render(request, 'aptrent/arrendadores.html')

@login_required
@check_user_type('arrendatario')
def arrendatarios_view(request):
    return render(request, 'aptrent/arrendatarios.html')


# Mantenedor Usuarios
def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Inicia sesión automáticamente después de registrarse
            user = form.save()
            login(request, user)
            # Redirige a la página principal o cualquier otra página
            return redirect('base')  # Cambia a la URL que desees
    else:
        form = CustomUserCreationForm()
    return render(request, 'aptrent/registro.html', {'form': form})


def custom_logout(request):
    # Cerrar sesión
    logout(request)
    # Redirigir a una página de confirmación
    return render(request, 'registration/logout.html')

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirigir según el tipo de usuario
            user_profile = user.userprofile  # Accede al perfil del usuario
            if user_profile.user_type == 'arrendatario':
                return redirect('arrendatarios')  # Redirige a la vista de arrendatarios
            elif user_profile.user_type == 'arrendador':
                return redirect('arrendadores')  # Redirige a la vista de arrendadores
            return redirect('home')  # Redirige al home si no tiene tipo
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

