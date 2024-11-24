from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import registro, index, custom_login, custom_logout, arrendadores_view, arrendatarios_view # La vista que crearemos para el registro
from .decorators import check_user_type

urlpatterns = [
    # URLS para gestion de usuairio
    path('registro/', registro, name='registro'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),    
    
    # Path arrendatarios y arrendadores
    path('arrendadores/', check_user_type('arrendador')(arrendadores_view), name='arrendadores'),
    path('arrendatarios/', check_user_type('arrendatario')(arrendatarios_view), name='arrendatarios'),

    
    # HomePage
    path('', index, name='base'),
]
