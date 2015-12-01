#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate --noinput

echo "$GIT_SHA" > static/revision
