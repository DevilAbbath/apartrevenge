from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Region, Comuna, Inmueble, SolicitudArriendo

# Register your models here.

# Aapartado de usuarios
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0  # No agregar filas vacías por defecto
# Registro del modelo User con el perfil
class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]  # Muestra el perfil en el formulario de creación/edición de usuario
    
    
# Mantenedor de Comunas y Regiones
class RegionAdmin(admin.ModelAdmin):
    list_display = ('numero_romano', 'nombre')
    search_fields = ('nombre', 'numero_romano')
    list_filter = ('numero_romano',)

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region')
    search_fields = ('nombre', 'region__nombre')
    list_filter = ('region',)
    
    
# Apartado de Inmuebles
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_inmueble', 'region', 'comuna', 'precio_mensual')
    search_fields = ('nombre', 'descripcion', 'region__nombre', 'comuna__nombre')
    list_filter = ('tipo_inmueble', 'region', 'comuna', 'precio_mensual')


# Mantenedor de asignaciones
class SolicitudArriendoAdmin(admin.ModelAdmin):
    list_display = ('id_solicitud', 'user__first_name', 'user__last_name', 'inmueble', 'fecha_solicitud', 'estado_solicitud')
    search_fields = ('user__first_name', 'user__last_name', 'inmueble__nombre', 'estado_solicitud')
    list_filter = ('estado_solicitud', 'fecha_solicitud')




admin.site.unregister(User)  # Desregistra el User admin para agregar el personalizado
admin.site.register(User, CustomUserAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(SolicitudArriendo, SolicitudArriendoAdmin)