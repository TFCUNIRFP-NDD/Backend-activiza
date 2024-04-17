#!/bin/sh

set -e

#Auto migrate para aplicar cambios en la BDD
python manage.py migrate
python manage.py collectstatic --no-input

uwsgi --socket :80 --master --enable-threads --module backend.wsgi