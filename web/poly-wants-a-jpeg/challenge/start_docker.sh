#!/bin/bash

docker build -t polywantsajpeg-4243 . && \
docker run -it -p 4243:4243 --rm --name polywantsajpeg-container polywantsajpeg-4243