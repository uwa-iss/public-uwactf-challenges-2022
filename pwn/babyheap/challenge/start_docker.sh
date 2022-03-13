#!/bin/bash -ex
make clean && make
docker build -t iss_ctf/babyheap .
docker run --name babyheap-container iss_ctf/babyheap:latest