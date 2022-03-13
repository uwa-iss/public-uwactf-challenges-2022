#!/bin/bash

docker build -t ping-of-death-1004 . && \
docker run -it -p 1004:1004 --rm --name ping-of-death-container ping-of-death-1004
