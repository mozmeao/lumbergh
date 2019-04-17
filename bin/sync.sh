#!/bin/bash

set -xf

aws s3 sync ./_site ${BUCKET_PATH} \
    --exclude "*" \
    $(jq .paths[] static/staticfiles.json | xargs -I {} echo -n "--include static/{}* ") \
    --cache-control "max-age=315360000,public,immutable" \
    --acl public-read \
    --delete

aws s3 sync ./_site ${BUCKET_PATH} \
    --include "*" \
    $(jq .paths[] static/staticfiles.json | xargs -I {} echo -n "--exclude static/{}* ") \
    --acl public-read \
    --delete
