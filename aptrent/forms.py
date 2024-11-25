from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Inmueble

class CustomUserCreationForm(UserCreationForm):
    # Campos adicionales de UserProfile
    rut = forms.CharField(max_length=12, required=True, label="RUT")
    telefono = forms.CharField(max_length=15, required=True, label="Teléfono")
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES, required=True, label="Tipo de Usuario")
    direccion = forms.CharField(max_length=255, required=True, label="Dirección")
    
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')  # Incluye los campos de User

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        # Crear UserProfile solo si no existe
        UserProfile.objects.update_or_create(
            user=user,
            defaults={
                'rut': self.cleaned_data['rut'],
                'telefono': self.cleaned_data['telefono'],
                'user_type': self.cleaned_data['user_type'],
                'direccion': self.cleaned_data['direccion']
            }
        )

        return user

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_totales', 'estacionamientos',
                  'habitaciones', 'banos', 'direccion', 'comuna', 'region', 'tipo_inmueble', 'precio_mensual']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'tipo_inmueble': forms.Select(choices=Inmueble.TIPO_INMUEBLE_CHOICES),
        }
