#!/bin/bash -ex
make clean && make
docker build -t iss_ctf/houseofwhat .
docker run --name houseofwhat-container iss_ctf/houseofwhat:latest