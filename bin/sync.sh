#!/bin/bash

# `-f` escapes `*`
set -xf
BUCKET_PATH=${BUCKET_PATH:-s3://mozilla-careers-stage}
BUCKET_NAME=${BUCKET_PATH:5}

# Set to true to update Cache-Control metadata for all static files.
GLOBAL_SET_METADATA=${GLOBAL_SET_METADATA:-false}

# Sync static assets first, before uploading other files that reference them.
# Set long live cache headers using `aws s3api` only to files that changed.
CHANGED_FILES=$(\
    ./bin/rclone --config ./bin/rclone.conf --no-update-modtime -v -P \
                 $(jq .paths[] static/staticfiles.json | xargs -I {} echo -n "--include static/{} ") \
                 sync ./_site ${BUCKET_PATH} 2>&1 | grep "Copied" | cut -d ":" -f 4)


if [ ${GLOBAL_SET_METADATA} = true ];
then
    CHANGED_FILES=$(jq .paths[] static/staticfiles.json -r | xargs -I {}  echo "static/{}")
fi

for file in ${CHANGED_FILES};
do
    metadata=$(
        aws s3api head-object \
            --bucket ${BUCKET_NAME} \
            --key ${file}
             )
    aws s3api copy-object \
        --acl public-read \
        --copy-source ${BUCKET_NAME}/${file} \
        --bucket  ${BUCKET_NAME} \
        --key ${file} \
        --metadata-directive REPLACE \
        --content-type $(echo $metadata | jq .ContentType) \
        --cache-control "max-age=315360000,public,immutable" \
        --metadata "{\"mtime\": $(echo $metadata | jq .Metadata.mtime)}"
done


# Sync the rest of the files.
./bin/rclone --config ./bin/rclone.conf \
       $(jq .paths[] static/staticfiles.json | xargs -I {} echo -n "--exclude static/{} ") \
       sync ./_site ${BUCKET_PATH}
