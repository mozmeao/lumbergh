#!/bin/sh

./bin/run-common.sh

echo "$GIT_SHA" > static/revision.txt

gunicorn careers.wsgi:application -b 0.0.0.0:${PORT:-8000} --log-file - --worker-class=${GUNICORN_WORKER_CLASS:-"meinheld.gmeinheld.MeinheldWorker"} -w ${WEB_CONCURRENCY:-2}
