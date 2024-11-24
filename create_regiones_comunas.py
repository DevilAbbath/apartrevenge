import os
import django
import json

# Configuración de Django para que el script acceda al entorno del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apartrevenge.settings")
django.setup()

from aptrent.models import Region, Comuna

def create_regiones_comunas():
    # Cargar el archivo JSON con la información de regiones y comunas
    with open('rc.json') as f:
        data = json.load(f)

    # Iterar sobre las regiones y crear las instancias en la base de datos
    for region_data in data['regions']:
        region = Region.objects.create(
            nombre=region_data['nombre'],
            numero_romano=region_data['numero_romano']  # Asegúrate que el modelo tenga este campo
        )
        
        # Crear las comunas asociadas a cada región
        for comuna_data in region_data['communes']:
            Comuna.objects.create(
                nombre=comuna_data['nombre'],
                region=region
            )
            print(f"Comuna {comuna_data['nombre']} en la región {region_data['nombre']} creada correctamente.")

if __name__ == "__main__":
    create_regiones_comunas()
