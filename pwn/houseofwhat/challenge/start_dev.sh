#!/bin/bash -ex
make clean && make
docker build -t iss_ctf/houseofwhat .
docker run -d \
    --name houseofwhat-container \
    --cap-add=SYS_PTRACE \
    --security-opt apparmor=unconfined \
    --security-opt seccomp=unconfined \
    iss_ctf/houseofwhat:latest
docker exec -it houseofwhat-container /bin/bash