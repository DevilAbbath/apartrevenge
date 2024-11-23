from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# Apartado de Usuarios
class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con User
    rut = models.CharField(max_length=12, unique=True)  # RUT único
    telefono = models.CharField(max_length=9, blank=True)  # Teléfono (opcional)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)  # Tipo de usuario
    direccion = models.CharField(max_length=200, blank=True)  # Dirección (opcional)

    def __str__(self):
        return self.user.username  # Devuelve el nombre de usuario como representación
    

# Gestor Comunas y Regiones
class Region(models.Model):
    numero_romano = models.CharField(max_length=10, unique=True)  # Ejemplo: "XIII"
    nombre = models.CharField(max_length=100, unique=True)       # Ejemplo: "Metropolitana de Santiago"

    def __str__(self):
        return f"{self.numero_romano} - {self.nombre}"

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)       # Ejemplo: "Providencia"
    region = models.ForeignKey('Region', on_delete=models.CASCADE)  # Relación con Region

    def __str__(self):
        return f"{self.nombre} ({self.region})"
    

# Inmuebles
class Inmueble(models.Model):
    # Mejor dejarlo limitado por un Choice para evitar mal tipado
    TIPO_INMUEBLE_CHOICES = (
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('oficina', 'Oficina'),
    )
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, blank=True, null=True)  # Relación con Comuna
    region = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)  # Relación con Region
    tipo_inmueble = models.CharField(max_length=50, choices=TIPO_INMUEBLE_CHOICES)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre
    

# Asignacion de inmueble
class SolicitudArriendo(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    
    # Relación con el modelo User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inmueble = models.ForeignKey('Inmueble', on_delete=models.CASCADE)
    fecha_solicitud = models.DateField()
    estado_solicitud = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada')
    ], default='pendiente')  # Valor por defecto 'pendiente'
    
    def __str__(self):
        return f"Solicitud {self.id_solicitud} - {self.user.first_name} {self.user.last_name}"
