#!/bin/bash

set -e

# sync from greenhouse
python manage.py sync_greenhouse

# build the static site
python manage.py build

# ping dead man snitch
curl "$DMS"
