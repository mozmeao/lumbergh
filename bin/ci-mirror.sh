#!/bin/bash -e

# Build an image that renders and copies static content to an S3 bucket
# Ping DMS when complete

export IMAGE=mozmeao/lumbergh-deploy:`git rev-parse --short HEAD`
docker build -f ./bin/Dockerfile . -t ${IMAGE}
docker run \
      -e AWS_ACCESS_KEY_ID \
      -e AWS_SECRET_ACCESS_KEY \
      -e BUCKET_PATH \
      -e DMS \
      -e CI_COMMIT_SHA \
      ${IMAGE}
