#!/bin/bash

docker build -t iamtheadmin-4246 . && \
docker run -it -p 4246:4246 --rm --name iamtheadmin-container iamtheadmin-4246 