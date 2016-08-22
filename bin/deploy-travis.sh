#!/bin/bash
set -e

DEIS=$1
APP=$2
NRAPP=$3

docker login -e "$DOCKER_EMAIL" -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"
docker push ${DOCKER_REPOSITORY}:${TRAVIS_COMMIT}

# Install deis client
curl -sSL http://deis.io/deis-cli/install.sh | sh
./deis login $DEIS --username $DEIS_USERNAME --password $DEIS_PASSWORD
./deis pull ${DOCKER_REPOSITORY}:${TRAVIS_COMMIT} -a $APP
curl -H "x-api-key:$NEWRELIC_API_KEY" \
     -d "deployment[app_name]=$NRAPP" \
     -d "deployment[revision]=$TRAVIS_COMMIT" \
     -d "deployment[user]=Travis" \
     https://api.newrelic.com/deployments.xml
