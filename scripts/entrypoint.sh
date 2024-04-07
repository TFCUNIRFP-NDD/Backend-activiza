#!/bin/sh

set -e

python manage.py collectstatic --no-input

uwsgi --socket :8000 --master --enable-threads --module dashpack.wsgi