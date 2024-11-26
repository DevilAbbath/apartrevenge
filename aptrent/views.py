from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.db.models import Exists, OuterRef
from .decorators import check_user_type
from .forms import CustomUserCreationForm, InmuebleForm, SolicitudArriendoForm
from .models import UserProfile, Inmueble, SolicitudArriendo

# Mantenedor de otras Paginas
def index(request):
    return render(request, 'aptrent/index.html')

@login_required
@check_user_type('arrendador')
def arrendadores_view(request):
    user = request.user
    inmuebles = Inmueble.objects.filter(propietario=user)
    return render(request, 'aptrent/arrendadores.html', {'inmuebles': inmuebles})

@login_required
@check_user_type('arrendatario')
def arrendatarios_view(request):
    # Excluir inmuebles con solicitudes pendientes
    inmuebles_con_solicitudes = SolicitudArriendo.objects.filter(
        inmueble=OuterRef('pk'),
        estado_solicitud='pendiente'
    )
    
    inmuebles = Inmueble.objects.filter(
        comuna__isnull=False, 
        region__isnull=False
    ).annotate(
        tiene_solicitud_pendiente=Exists(inmuebles_con_solicitudes)
    ).filter(
        tiene_solicitud_pendiente=False
    )
    
    return render(request, 'aptrent/arrendatarios.html', {'inmuebles': inmuebles})

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



# Mantenedor Inmueble
@login_required
def agregar_inmueble(request):    
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.propietario = request.user
            inmueble.save()
            messages.success(request, 'Inmueble agregado con éxito.')
            return redirect('arrendadores')
    else:
        form = InmuebleForm()

    return render(request, 'aptrent/inmuebles/agregar_inmueble.html', {'form': form})

@login_required
def editar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id, propietario=request.user)  # Solo el propietario puede editar
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inmueble actualizado con éxito.')
            return redirect('arrendadores')
    else:
        form = InmuebleForm(instance=inmueble)

    return render(request, 'aptrent/inmuebles/editar_inmueble.html', {'form': form})

def lista_inmuebles(request):
    user = request.user

    if user.is_authenticated:
        user_profile = UserProfile.objects.get(user=user)
        if user_profile.user_type == 'arrendador':
            inmuebles = Inmueble.objects.filter(propietario=user, comuna__isnull=False, region__isnull=False)
        else:
            inmuebles = Inmueble.objects.filter(comuna__isnull=False, region__isnull=False)
    else:
        # Para usuarios no autenticados, muestra todos los inmuebles disponibles
        print("Usuario no autenticado.")
        inmuebles = Inmueble.objects.filter(comuna__isnull=False, region__isnull=False)

    return render(request, 'aptrent/inmuebles/lista_inmuebles_publica.html', {'inmuebles': inmuebles})

@login_required
def eliminar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)

    # Verificar que el usuario sea el propietario
    if inmueble.propietario != request.user:
        return PermissionDenied("No tienes permiso para eliminar este inmueble.")
    
    if request.method == 'POST':
        inmueble.delete()
        return redirect('arrendadores')
    
    return render(request, 'aptrent/inmuebles/eliminar_inmueble.html', {'inmueble': inmueble})



# Mantenedor Solicitudes
@login_required
def crear_solicitud_arriendo(request, inmueble_id):
    # Verificar que el usuario es arrendatario
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if user_profile.user_type != 'arrendatario':
        return redirect('index')

    # Obtener el inmueble por ID
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)

    if request.method == 'POST':
        form = SolicitudArriendoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.user = request.user
            solicitud.inmueble = inmueble
            solicitud.save()
            return redirect('arrendatarios')  # Redirigir a la lista después de guardar
    else:
        form = SolicitudArriendoForm(initial={'inmueble': inmueble})

    return render(request, 'aptrent/solicitudes/crear_solicitud.html', {'form': form, 'inmueble': inmueble})

@login_required
def listar_solicitudes(request):
    # Filtrar solicitudes realizadas por el usuario autenticado
    solicitudes = SolicitudArriendo.objects.filter(user=request.user).select_related('inmueble')
    return render(request, 'aptrent/solicitudes/listar_solicitudes.html', {'solicitudes': solicitudes})

@login_required
def eliminar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudArriendo, id_solicitud=solicitud_id, user=request.user)
    
    if request.method == 'POST':
        solicitud.delete()
        messages.success(request, 'La solicitud ha sido eliminada con éxito.')
        return redirect('arrendatarios')  # Reemplaza con el nombre de tu vista de "Mis solicitudes"
    
    return render(request, 'aptrent/solicitudes/confirmar_eliminar.html', {'solicitud': solicitud})