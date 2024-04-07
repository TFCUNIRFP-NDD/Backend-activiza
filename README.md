# Dashpack - A dashboard for ticketing systems WORK IN PROGRESS
A dashboard made to easily provide stadistics to technical ticketing systems. See the most important data beautifuly and fast. Production and development ready with Docker.

## Marketing To-Do
Lorem ipsum

# Building and testing

## Requirements
* Docker (have it running `systemctl start docker`)
* Docker-compose
* Python 3.6 >= (Has been tested in 3.6 and 3.9)

## Development
Use `docker-compose.yml` for development, it uses the Django built in `runserver`. 

The application is already setup for development. The sqlite database comes with data I have used for development. The username and password is `root`. You may use it or create a new file and follow the steps of creating a new DB of the production tutorial, but you won't have any dummy data.

## Production
Use `docker-compose-deploy.yml` for development, it NGINX and UWSGI to deliver the app. Edit the `ALLOWED_HOSTS` variable with the domain/s you gonna use. 

Change the `settings.py` with the production database settings, remember to change the user and password in the settings and the `.yml` file.

Change the secret key in the `.yml` file.

Once the server is up and running, we need to create the database, Django makes it easy. Run the migrations:

`sudo docker-compose exec dashpack python manage.py migrate`

Now create a superuser:

`sudo docker-compose exec dashpack python manage.py createsuperuser`

## FAQ
* The API is securely set up to be used only with superusers via tokens. More info about tokens and authentication in Django Rest Framework [here](https://www.django-rest-framework.org/api-guide/authentication/).

* I f*cked up! How do I remove everything inside the containers? Check the containers ID with `sudo docker ps -a` and delete them with `sudo docker stop IDhere otherID`. Then proceed to nuke everything inside of Docker (WARNING THIS WILL REMOVE ALL CONTAINERS AND DATA) with `sudo docker system prune -a`. Yes this has happened to me so much that I needed to do a FAQ to remember it.
