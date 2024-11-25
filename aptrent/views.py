from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .decorators import check_user_type
from .forms import CustomUserCreationForm
from .models import UserProfile

# Mantenedor de otras Paginas
def index(request):
    return render(request, 'aptrent/index.html')

@login_required
@check_user_type('arrendador')
def arrendadores_view(request):
    return render(request, 'aptrent/arrendadores.html')

@login_required
@check_user_type('arrendatario')
def arrendatarios_view(request):
    return render(request, 'aptrent/arrendatarios.html')

def handler403(request, exception):
    messages.error(request, "No tienes permiso para acceder a esta página.")
    return redirect('index')

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
            return redirect('index')  # Cambia a la URL que desees
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


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        # Actualizar datos del usuario
        request.user.email = email
        request.user.save()

        # Actualizar datos del perfil
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.telefono = telefono
        user_profile.direccion = direccion
        user_profile.save()

        messages.success(request, "Tu perfil ha sido actualizado correctamente.")
        return redirect('perfil')

    return render(request, 'aptrent/perfil.html')