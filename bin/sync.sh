#!/bin/bash

# `-f` escapes `*`
set -xf

BUCKET_NAME=${BUCKET_PATH:5}

# Sync static assets first, before uploading other files that reference them.
# Set long live cache headers using `aws s3api` only to files that changed.
./bin/rclone --config ./bin/rclone.conf --no-update-modtime -v \
       $(jq .paths[] static/staticfiles.json | xargs -I {} echo -n "--include static/{} ") \
       sync . ${BUCKET_PATH} 2>&1 | grep "Copied" | cut -d ":" -f 4 | xargs -I '{}' aws s3api copy-object \
                                                                        --acl public-read \
                                                                        --copy-source ${BUCKET_NAME}/'{}' \
                                                                        --bucket  ${BUCKET_NAME} \
                                                                        --key '{}' \
                                                                        --metadata-directive REPLACE \
                                                                        --cache-control "max-age=315360000,public,immutable"


# Sync the rest of the files.
./bin/rclone --config ./bin/rclone.conf --no-update-modtime \
       $(jq .paths[] static/staticfiles.json | xargs -I {} echo -n "--exclude static/{} ") \
       sync . ${BUCKET_PATH}
