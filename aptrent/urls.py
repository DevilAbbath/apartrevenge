from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .decorators import check_user_type
from .views import (
    registro, 
    index, 
    custom_login, 
    custom_logout, 
    arrendadores_view, 
    arrendatarios_view, 
    editar_perfil,
    agregar_inmueble, 
    editar_inmueble, 
    eliminar_inmueble, 
    lista_inmuebles,
    crear_solicitud_arriendo,
    listar_solicitudes,
    eliminar_solicitud

)

urlpatterns = [
    
    # URLS para gestion de usuairio
    path('registro/', registro, name='registro'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),    
    path('perfil/', editar_perfil, name='perfil'),
    
    # Path arrendadores
    path('arrendadores/', check_user_type('arrendador')(arrendadores_view), name='arrendadores'),
    path('inmuebles/agregar/', check_user_type('arrendador')(agregar_inmueble), name='agregar_inmueble'),
    path('inmuebles/editar/<int:id>/', check_user_type('arrendador')(editar_inmueble), name='editar_inmueble'),
    path('inmuebles/eliminar/<int:id>/', check_user_type('arrendador')(eliminar_inmueble), name='eliminar_inmueble'),

    # Path Arremdatarios
    path('arrendatarios/', check_user_type('arrendatario')(arrendatarios_view), name='arrendatarios'),
    path('solicitudes/', listar_solicitudes, name='listar_solicitudes'),
    path('solicitudes/crear/<int:inmueble_id>/', crear_solicitud_arriendo, name='crear_solicitud_arriendo'),  
    path('solicitudes/eliminar/<int:solicitud_id>/', eliminar_solicitud, name='eliminar_solicitud'),


    # Public Pages
    path('', index, name='index'),
    path('inmuebles/', lista_inmuebles, name='lista_inmuebles'),

]
