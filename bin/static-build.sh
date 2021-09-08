#!/bin/bash

./manage.py build

./bin/mirror.sh

cp -R ./_site/v1/listings ./static-build/listings

mkdir ./static-build/v1

cp -R ./_site/v1/position ./static-build/v1/position