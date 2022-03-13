#!/bin/bash

docker build -t oraclewebtoken-4244 . && \
docker run -it -p 4244:4244 -v $(pwd)/app/html:/app/html --rm --name oraclewebtoken-container oraclewebtoken-4244