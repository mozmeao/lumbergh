#!/bin/bash
EXIT=0
BASE_URL=${1:-http://careers.mozilla.org}
URLS=(
    "/"
    "/listings/"
    "/feed/"
    "/university/"
    "/robots.txt"
    "/contribute.json"
)

function check_http_code {
    echo -n "Checking URL ${1} "
    curl -L -s -o /dev/null -I -w "%{http_code}" $1 | grep ${2:-200} > /dev/null
    if [ $? -eq 0 ];
    then
        echo "OK"
    else
        echo "Failed"
        EXIT=1
    fi
}

for url in ${URLS[*]}
do
    check_http_code ${BASE_URL}${url}
done

# Check an invalid position which must throw 404. Not ideal but will surface
# 500s
check_http_code ${BASE_URL}/position/gh/1 404

exit ${EXIT}
