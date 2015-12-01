#!/bin/sh

./bin/run-common.sh

python manage.py collectstatic --noinput
echo "$GIT_SHA" > static/revision.txt

gunicorn careers.wsgi:application -b 0.0.0.0:${PORT:-8000} --log-file -
