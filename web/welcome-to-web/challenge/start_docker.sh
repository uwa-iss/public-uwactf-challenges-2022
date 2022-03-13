#!/bin/bash

docker build -t welcome-to-web-4245 . && \
docker run -it -p 4245:4245 --rm --name welcome-to-web-container welcome-to-web-4245
