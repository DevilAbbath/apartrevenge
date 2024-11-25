from django.shortcuts import redirect
from django.contrib import messages
from .models import UserProfile

def check_user_type(user_type):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # Verificar si el usuario está autenticado
            if not request.user.is_authenticated:
                messages.error(request, "Debes iniciar sesión para acceder a esta página.")
                return redirect('index')  # Redirigir al inicio

            # Obtener el perfil del usuario
            try:
                user_profile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                messages.error(request, "No se encontró un perfil asociado a este usuario.")
                return redirect('index')  # Redirigir al inicio

            # Validar el tipo de usuario
            if user_profile.user_type != user_type:
                messages.error(request, "No tienes permiso para acceder a esta página.")
                return redirect('index')  # Redirigir al inicio

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
