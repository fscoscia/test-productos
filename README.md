## Requerimientos

-   Python >= 3.7
-   Pipenv

## Aprobación de usuarios

Para aprobar un usuario dirigirse a la sección usuarios en el administrador de django, seleccionar los usuarios a aprobar y seleccionar la acción "Aprobar usuario".

## Entorno de desarrollo

1. En la carpeta raíz, crea un archivo `.env` con el siguiente contenido:

    ```
        DEBUG = True
        SECRET_KEY = supersecretkey
        ALLOWED_HOSTS = *
    ```

2. Instala las dependencias del proyecto:

    ```bash
    pipenv install
    ```

3. Ejecuta las migraciones y crea un superusuario:

    ```bash
    pipenv run python manage.py migrate
    pipenv run python manage.py createsuperuser
    ```

4. Ejecuta el servidor de desarrollo:

    ```bash
    pipenv run python manage.py runserver
    ```
