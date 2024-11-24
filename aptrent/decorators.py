from django.core.exceptions import PermissionDenied
from .models import UserProfile

def check_user_type(user_type):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # Obtener el perfil del usuario
            user_profile = UserProfile.objects.get(user=request.user)

            # Validar el tipo de usuario
            if user_profile.user_type != user_type:
                raise PermissionDenied("No tienes permiso para acceder a esta página.")
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
