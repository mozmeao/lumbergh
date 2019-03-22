#!/bin/bash

# https://docs.gitlab.com/ce/ci/variables/README.html
cd ${CI_PROJECT_DIR}

export IMAGE=mozmeao/lumbergh-deploy:`git rev-parse --short HEAD`
docker build -f ./Dockerfile.static . -t ${IMAGE}
docker run -it \
      -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
      -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
      -e BUCKET_PATH="${BUCKET_PATH}" \
      -e DMS="${DMS}" \
      ${IMAGE} 
echo "Done"