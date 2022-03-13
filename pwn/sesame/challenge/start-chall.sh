#!/bin/bash -ex
make clean && make
docker build -t iss_ctf/sesame .
docker run --name sesame-container iss_ctf/sesame:latest