#!/usr/bin/env bash
echo "Running build acceptance tests..."

for dir in listings position university feed
do
    if [ ! -d $dir ];
    then
       echo "Error: Directory ${dir} does not exist!";
       exit 1;
    fi
done

for file in index.html robots.txt contribute.json feed/index.html listings/index.html university/index.html; do
    if [ ! -f $file ];
    then
        echo "Error: File ${file} does not exist!";
        exit 1;
    fi
done

LISTED_JOB_COUNT=$(grep -c 'class="position"' listings/index.html)

if [ $LISTED_JOB_COUNT -eq 0 ];
then
    echo "Error: No jobs posted!";
    exit 1;
fi

INCLUDED_JOB_COUNT=$(find position/gh/ -type d -not -path position/gh/  | wc -l)

if [ ${LISTED_JOB_COUNT} -ne ${INCLUDED_JOB_COUNT} ];
then
    echo "Error: Number of listed jobs (${LISTED_JOB_COUNT}) doesn't much number of included jobs (${INCLUDED_JOB_COUNT})!";
    exit 1;
fi

echo "Success: Done!"
