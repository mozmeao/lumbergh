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

wget --header "Host: ${CAREERS_HOST:-careers.mozilla.org}" \
     --reject-regex "(.*)\?(.*)|static/(.*)" \
     --mirror \
     -nH -p -E http://0.0.0.0:8000/ http://0.0.0.0:8000/contribute.json

# Copy all static directory
cp -rp ../static .

# Convert all absolute links to relative. Wget's `-k` option won't operate on
# non-downloaded files and we exclude `/static` URLs.
find . -name \*.html | xargs sed -i 's/http:\/\/0.0.0.0:8000//'

# Remove references to index.html
find . -name \*.html -exec sed -i -e 's/index.html//'  {} \;

# Add state
echo "$COMMIT_REF" > static/revision.txt

echo "Mirroring complete"
