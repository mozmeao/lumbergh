#!/bin/bash

# `-f` escapes `*`
set -xf

echo "Before Syncs"
echo $(date +%s)

# Sync static assets first, before uploading other files that reference them.
# Set long live cache headers.
aws s3 sync ./_site ${BUCKET_PATH} \
    --exclude "*" \
    $(jq .paths[] static/staticfiles.json | xargs -I {} echo -n "--include static/{}* ") \
    --cache-control "max-age=315360000,public,immutable" \
    --acl public-read \
    --delete

echo "After Static Sync, before Non-static Sync"
echo $(date +%s)

# Sync the rest of the files.
aws s3 sync ./_site ${BUCKET_PATH} \
    --include "*" \
    $(jq .paths[] static/staticfiles.json | xargs -I {} echo -n "--exclude static/{}* ") \
    --acl public-read \
    --delete

echo "After Static Syncs"
echo $(date +%s)
