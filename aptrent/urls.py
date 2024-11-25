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
    lista_inmuebles

)

urlpatterns = [
    
    # URLS para gestion de usuairio
    path('registro/', registro, name='registro'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),    
    path('perfil/', editar_perfil, name='perfil'),
    
    # Path arrendatarios y arrendadores
    path('arrendadores/', check_user_type('arrendador')(arrendadores_view), name='arrendadores'),
    path('arrendatarios/', check_user_type('arrendatario')(arrendatarios_view), name='arrendatarios'),
    path('inmuebles/agregar/', check_user_type('arrendador')(agregar_inmueble), name='agregar_inmueble'),
    path('inmuebles/editar/<int:id>/', check_user_type('arrendador')(editar_inmueble), name='editar_inmueble'),
    path('inmuebles/eliminar/<int:id>/', check_user_type('arrendador')(eliminar_inmueble), name='eliminar_inmueble'),

    # Public Pages
    path('', index, name='index'),
    path('inmuebles/', lista_inmuebles, name='lista_inmuebles'),

]
