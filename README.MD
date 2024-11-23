# Plataforma de Arrendamiento Inmobiliario
# Hito 2 - - Implementación de autenticación de usuarios usando django-auth

## Descripción

Este proyecto corresponde al Hito 2 del desafío de la plataforma de arrendamiento inmobiliario. El objetivo es crear un sistema de autenticación de usuarios, el cual permita a los usuarios registrarse, iniciar sesión
y cerrar sesión en el sitio web, así como gestionar permisos y grupos de usuarios.

## Requerimientos

- Django 5.1.3
- Python 3.12+
- PostgreSQL

## Funcionalidad en el Panel de vista web

1. **Iniciar Sesion**: Redirecciona a un form para poder ingresar las credenciales de acceso al sitio.
2. **Cerrar Sesion**: Eliminar del aplicativo la informacion sobre si existe un usuario conectado.
3. **Registrarse**: Usando los forms permitir el ingreso de un nuevo usuario definiendo su funcion y datos adicionales.

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
    Visita http://127.0.0.1:8000/admin para gestionar los modelos de Inmueble, UserProfile y SolicitudArriendo.



## Conclusion

    Podemos usar admin.site.register() habilita los modelos en el panel de administración.

    Los operadores list_display, search_fields, y list_filter personalizan y mejoran la experiencia del usuario para la gestión de datos.


### Print de lo esperado

![img1](print/Hito2/user.png)

![img2](print/Hito2/comuna.png)

![img3](print/Hito2/inmueble.png)

![img4](print/Hito2/regiones.png)

![img5](print/Hito2/solicitudarr.png)




Autor
Nombre: [Erick-Jaime-Jara]
Correo: [alucard.erick.mega@gmail.com]