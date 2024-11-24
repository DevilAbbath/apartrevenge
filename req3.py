import os
import django

# Configurar el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apartrevenge.settings') 
django.setup()

# Importar los modelos de Django
from aptrent.models import Inmueble, Region

# Función para consultar y guardar los inmuebles por región
def consultar_inmuebles_por_region():
    # Abrir el archivo de texto donde guardaremos los resultados
    with open('inmuebles_por_region.txt', 'w', encoding='utf-8') as file:
        # Obtener todas las regiones
        regiones = Region.objects.all()

        # Recorrer cada región
        for region in regiones:
            # Escribir el nombre de la región en el archivo
            file.write(f'Región: {region.nombre}\n')

            # Consultar los inmuebles de esta región
            inmuebles = Inmueble.objects.filter(region=region).values('nombre', 'descripcion')

            # Escribir cada inmueble en el archivo
            for inmueble in inmuebles:
                file.write(f" - {inmueble['nombre']}: {inmueble['descripcion']}\n")

            file.write("\n" + "-"*50 + "\n")  # Separador entre regiones

    print("Consulta y archivo generados con éxito.")

# Ejecutar la función
consultar_inmuebles_por_region()
