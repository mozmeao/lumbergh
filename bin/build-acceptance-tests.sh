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

JOB_COUNT=$(grep -c 'class="position"' listings/index.html)

if [ $JOB_COUNT -eq 0 ];
then
    echo "Error: No jobs posted!";
    exit 1;
fi

echo "Success: Done!"
