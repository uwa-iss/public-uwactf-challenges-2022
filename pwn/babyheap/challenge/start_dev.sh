#!/bin/bash -ex
make clean && make
docker build -t iss_ctf/babyheap .
docker run -d \
    --name babyheap-container \
    --cap-add=SYS_PTRACE \
    --security-opt apparmor=unconfined \
    --security-opt seccomp=unconfined \
    iss_ctf/babyheap:latest
docker exec -it babyheap-container /bin/bash