#!/bin/bash -ex
make clean && make
docker build -t iss_ctf/sesame .
docker run -d \
    --name sesame-container \
    --cap-add=SYS_PTRACE \
    --security-opt apparmor=unconfined \
    --security-opt seccomp=unconfined \
    iss_ctf/sesame:latest
docker exec -it sesame-container /bin/bash
