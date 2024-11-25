# Plataforma de Arrendamiento Inmobiliario
# Hito 2 - - Implementación de autenticación de usuarios usando django-auth

## Descripción

Este proyecto corresponde al Hito 3 del desafío de la plataforma de arrendamiento inmobiliario. Se han realizado diversas tareas para poblar la base de datos, consultar y generar reportes de inmuebles para arriendo, todo utilizando Django, migraciones y consultas SQL a través de scripts de Python.

## Requerimientos

- Django 5.1.3
- Python 3.12+
- PostgreSQL

## Funcionalidad en el Panel de vista web

1. **Iniciar Sesion**: Redirecciona a un form para poder ingresar las credenciales de acceso al sitio.
2. **Cerrar Sesion**: Eliminar del aplicativo la informacion sobre si existe un usuario conectado.
3. **Registrarse**: Usando los forms permitir el ingreso de un nuevo usuario definiendo su funcion y datos adicionales.
4. **Identificacion de Usuario**: En base al tipo de usuario es derivado a su portal 

## Pasos para la Instalación

1. **Clonar el Repositorio**:
   ```bash
   git clone <repositorio-url>
   cd <repositorio>

2. **Configuración de la Base de Datos**:

    - Crea la base de datos en PostgreSQL.
    - Configura DATABASES en settings.py.

3. **Migraciones**: 
    Ejecuta las migraciones para crear las tablas en la base de datos:

        ```bash
        python manage.py migrate

4. **Crear un Superusuario**: 
    Para acceder al panel de administración:

    ```bash
    python manage.py createsuperuser

5. **Iniciar el Servidor**: 
    Ejecuta el servidor de desarrollo de Django:

    ```bash
    python manage.py runserver

6. **Acceder al Panel de Admin**: 
    Visita http://127.0.0.1:8000/ para acceder e interectuar con los distintos operadores.


# Resumen del Trabajo Realizado

## **1. Página web para agregar nuevos inmuebles (Arrendadores)**
- **a. Rutas para agregar inmuebles:**  
  Se configuraron las rutas en `urls.py` para acceder a la vista `agregar_inmueble`, específica para que los arrendadores puedan añadir nuevas propiedades.
- **b. Formulario basado en el modelo:**  
  Se creó un formulario en `forms.py` utilizando el modelo `Inmueble`, limitando los campos al usuario autenticado (propietario).
- **c. Función para guardar el objeto:**  
  Se implementó la función `agregar_inmueble` en `views.py`, verificando que solo arrendadores puedan crear inmuebles. El formulario valida los datos y guarda el objeto en la base de datos.

---

## **2. Página web para actualizar y eliminar inmuebles existentes (Arrendadores)**
- **a. Rutas para actualizar y eliminar inmuebles:**  
  Se configuraron rutas en `urls.py` para las vistas `actualizar_inmueble` y `eliminar_inmueble`, accesibles solo para arrendadores autenticados.
- **b. Formulario en base al modelo:**  
  El formulario para actualizar inmuebles se generó en `forms.py`, utilizando nuevamente el modelo `Inmueble`. Este formulario precarga datos para su edición.
- **c. Funciones para actualizar y eliminar inmuebles:**
  - **Actualizar:**  
    La función `actualizar_inmueble` en `views.py` permite a los arrendadores editar propiedades que les pertenecen, utilizando lógica para asegurar permisos.
  - **Eliminar:**  
    La función `eliminar_inmueble` solicita confirmación antes de eliminar el inmueble asociado al usuario autenticado.

---

## **3. Página web para que los arrendatarios vean inmuebles disponibles**
- **a. Rutas para listar inmuebles:**  
  Se definió la ruta `lista_inmuebles` en `urls.py`, accesible tanto para usuarios autenticados como no autenticados.
- **b. Vista y controlador:**  
  Se implementó la vista `lista_inmuebles` en `views.py`, la cual filtra los inmuebles disponibles:
  - **Para arrendadores:**  
    Muestra solo inmuebles creados por el usuario autenticado.
  - **Para arrendatarios y visitantes no autenticados:**  
    Muestra la oferta completa de inmuebles disponibles.
- El archivo `lista_inmuebles.html` se diseñó para adaptarse dinámicamente, mostrando el navbar y el footer solo cuando el usuario no está autenticado.

---

## **Resultados**
- Las funcionalidades cumplen con los requerimientos establecidos, brindando una interfaz básica y dinámica para arrendadores y arrendatarios.
- Se aseguraron las restricciones de acceso mediante validaciones de autenticación y roles (`arrendador` y `arrendatario`).



### Print de los resultados

![img1](print/Hito4/img1.png)

![img2](print/Hito4/img2.png)

![img3](print/Hito4/img3.png)

![img4](print/Hito4/img4.png)


Autor
Nombre: [Erick-Jaime-Jara]
Correo: [alucard.erick.mega@gmail.com]