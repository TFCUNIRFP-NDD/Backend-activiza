#!/bin/sh

set -e

python manage.py collectstatic --noinput

python manage.py migrate
uwsgi --socket :8000 --master --enable-threads --module backend.wsgi

#Auto migrate para aplicar cambios en la BDD

#python manage.py runserver 0.0.0.0:80