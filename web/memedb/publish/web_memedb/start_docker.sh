#!/bin/bash

docker build -t memeapi-4242 . && \
docker run -it -p 4242:4242 --rm --name memeapi-container memeapi-4242