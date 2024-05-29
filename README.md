# Activiza backend

API Rest creada en Python y Django

## Marketing To-Do

Lorem ipsum

# Building and testing

## Requirements

-   Docker
-   Docker-compose
-   Python >= 3.12 

## Development

Lanzar `docker-compose.yml` con `sudo docker-compose up --build --force-recreate -d` usa el servicio de Django `runserver`.

Esta automáticamente configurado para migrar la base de datos (crear tablas en Django) y lanzar la API en local, en el puerto 80 (HTTP). Esta API no es segura tal como está construida, debido a la finalidad del TFC se ha prioritizado desarrollar características antes que centrarse en crear un servidor dockerizado de NGINX con certificados para poder brindarla con un servidor "de verdad" de forma segura.

## FAQ

-   The API is securely set up to be used only with superusers via tokens. More info about tokens and authentication in Django Rest Framework [here](https://www.django-rest-framework.org/api-guide/authentication/).
