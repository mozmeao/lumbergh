#!/bin/bash
set -xe

GREENHOUSE_URL="https://api.greenhouse.io/v1/boards/mozilla/jobs/?content=true"

cp env-build .env

ESCAPED_SITE_URL=${ESCAPED_SITE_URL:-"http:\/\/localhost:8000"}

# Allow search engine crawling in production only
if [[ ${CI_COMMIT_REF_NAME} == "prod" ]];
then
    echo "ENGAGE_ROBOTS=True" >> .env
else
    echo "ENGAGE_ROBOTS=False" >> .env
fi

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py sync_greenhouse

gunicorn careers.wsgi:application --daemon -b 0.0.0.0:8000 -w 2 --timeout 300

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
# -e robots=off: Causes it to ignore robots.txt for that domain
#
# --quiet: Turn off output.
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
     -e robots=off \
     --quiet \
     -nH -p  http://0.0.0.0:8000/ http://0.0.0.0:8000/contribute.json http://0.0.0.0:8000/404.html http://0.0.0.0:8000/robots.txt http://0.0.0.0:8000/internships/

# Copy static directory
cp -rp ../static .

# Set correct site url for RSS feed.
sed -i "s/http:\/\/0.0.0.0:8000/${ESCAPED_SITE_URL}/g" feed/index.html

# Convert all absolute links to relative. Wget's `-k` option won't operate on
# non-downloaded files and we exclude `/static` URLs.
find . -name \*.html | xargs sed -i 's/http:\/\/0.0.0.0:8000//g'

# Remove references to index.html
find . -name \*.html -exec sed -i -e 's/index.html//g' {} \;

# Add state
echo "$CI_COMMIT_SHA" > static/revision.txt

# Run build acceptance tests
.$(dirname "$0")/build-acceptance-tests.sh

echo "Generation complete"
