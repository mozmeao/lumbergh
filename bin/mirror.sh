#!/bin/bash
set -xe

GREENHOUSE_URL="https://api.greenhouse.io/v1/boards/mozilla/jobs/?content=true"

cp env-build .env

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py sync_greenhouse

gunicorn careers.wsgi:application --daemon -b 0.0.0.0:8000 -w 2

# Wait for site to come online
CHECK_PORT=8000 CHECK_HOST=0.0.0.0 ./bin/takis

mkdir -vp _site
pushd _site

# --reject-regex: Don't mirror URLs that include `?` i.e. with URL parameters or
#                 URLs that contain with /static/ (which we will directly copy
#                 from the ./static/ folder later)
#
# --mirror: Turn on options suitable for mirroring: recursion and time-stamping,
#           sets infinite recursion depth
#
# -nH: Don't create host directories. If not included the final directory
#      structure would be _site/0.0.0.0:8000/..
#
# -p: This option causes Wget to download all the files that are necessary to
#     properly display a given HTML page. This includes such things as inlined
#     images, sounds, and referenced stylesheets.
#
wget --reject-regex "(.*)\?(.*)|/static/(.*)" \
     --mirror \
     -nH -p  http://0.0.0.0:8000/ http://0.0.0.0:8000/contribute.json http://0.0.0.0:8000/404.html

# Copy static directory
cp -rp ../static .

# Convert all absolute links to relative. Wget's `-k` option won't operate on
# non-downloaded files and we exclude `/static` URLs.
find . -name \*.html | xargs sed -i 's/http:\/\/0.0.0.0:8000//'

# Remove references to index.html
find . -name \*.html -exec sed -i -e 's/index.html//' {} \;

# Add state
echo "$COMMIT_REF" > static/revision.txt

# Add custom headers
cp ../netlify-headers ./_headers

# Add custom redirects
cp ../netlify-redirects ./_redirects

# Run build acceptance tests
.$(dirname "$0")/build-acceptance-tests.sh

echo "Generation complete"
