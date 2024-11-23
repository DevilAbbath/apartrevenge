from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import registro, index, custom_logout  # La vista que crearemos para el registro


urlpatterns = [
    # URLS para gestion de usuairio
    path('registro/', registro, name='registro'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),    
    
    # HomePage
    path('', index, name='base'),
]
