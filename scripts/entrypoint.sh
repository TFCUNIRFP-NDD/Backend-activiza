#!/bin/sh

set -e

python manage.py collectstatic --no-input

uwsgi --socket :80 --master --enable-threads --module backend.wsgi