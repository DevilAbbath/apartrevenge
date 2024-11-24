import os
import django

# Configurar el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apartrevenge.settings') 
django.setup()

# Importar los modelos de Django
from aptrent.models import Inmueble, Comuna

# Función para consultar y guardar los inmuebles
def consultar_inmuebles():
    # Abrir el archivo de texto donde guardaremos los resultados
    with open('inmuebles_por_comuna.txt', 'w', encoding='utf-8') as file:
        # Obtener todas las comunas
        comunas = Comuna.objects.all()

        # Recorrer cada comuna
        for comuna in comunas:
            # Escribir el nombre de la comuna en el archivo
            file.write(f'Comuna: {comuna.nombre}\n')

            # Consultar los inmuebles de esta comuna
            inmuebles = Inmueble.objects.filter(comuna=comuna).values('nombre', 'descripcion')

            # Escribir cada inmueble en el archivo
            for inmueble in inmuebles:
                file.write(f" - {inmueble['nombre']}: {inmueble['descripcion']}\n")

            file.write("\n" + "-"*50 + "\n")  # Separador entre comunas

    print("Consulta y archivo generados con éxito.")

# Ejecutar la función
consultar_inmuebles()
