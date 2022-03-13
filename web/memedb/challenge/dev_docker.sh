#!/bin/bash

docker build -t memeapi-4242 . && \
docker run -it -p 4242:4242 -v $(pwd)/app/html:/app/html --rm --name memeapi-container memeapi-4242