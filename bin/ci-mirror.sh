#!/bin/bash -e

export IMAGE=mozmeao/lumbergh-deploy:`git rev-parse --short HEAD`
docker build -f ./bin/Dockerfile . -t ${IMAGE}
docker run \
      -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
      -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
      -e BUCKET_PATH="${BUCKET_PATH}" \
      -e DMS="${DMS}" \
      ${IMAGE} 
