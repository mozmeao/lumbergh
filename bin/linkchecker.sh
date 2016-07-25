#!/bin/bash
set -xe
HOST=${HOST:-"https://careers.mozilla.org"}
docker run -v `pwd`:/app python:2 bash -c "cd /app && pip install linkchecker requests==2.9 && linkchecker --check-extern $HOST"
