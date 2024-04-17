#!/bin/sh

set -e

#Auto migrate para aplicar cambios en la BDD
python manage.py migrate
python manage.py runserver 0.0.0.0:80