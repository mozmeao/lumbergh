#!/usr/bin/env bash
echo "Running build acceptance tests..."

for dir in listings position internships feed
do
    if [ ! -d $dir ];
    then
       echo "Error: Directory ${dir} does not exist!";
       exit 1;
    fi
done

for file in index.html robots.txt contribute.json feed/index.html listings/index.html internships/index.html; do
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

# array to hold bad urls
declare -a bad_urls

# loop through all href destination starting with http in index.html
# this will target all external urls
# (we shouldn't need to check other files...yet)
while read -r url; do
    # get the http status code
    # instagram urls fail if using --head
    urlstatus=$(curl -o /dev/null --silent --write-out '%{http_code}' "$url")

    # if http status code is >= 400 or < 200, it's a problem
    if [[ "$urlstatus" -ge 400 || "$urlstatus" -lt 200 ]];
    then
        bad_urls+=("$url")
    fi
done < <(sed -n 's/.*href="\(http[^"]*\).*/\1/p' index.html)

# if we captured any bad urls, echo them out and return w/exit code 1
if [ "${#bad_urls[@]}" -gt 0 ];
then
    echo "Unreachable external URLs found:";
    echo ${bad_urls[*]};
    exit 1;
fi

echo "Success: Done!"
