FROM ubuntu:bionic

ARG HOMEDIR="/chall"
ARG BINARY="houseofwhat"
WORKDIR "/chall"

RUN apt-get update; apt-get -y install socat gdb && rm -rf /var/lib/apt/*
RUN useradd --no-create-home --home-dir "${HOMEDIR}" issusr

RUN mkdir -p /chall/lib
COPY houseofwhat ${HOMEDIR}/
COPY ./lib/ld.so ./lib/libc.so.6 /chall/lib/
COPY flag.txt ${HOMEDIR}/
RUN chmod 555 ${HOMEDIR}/lib/ld.so ${HOMEDIR}/lib/libc.so.6
RUN chmod 555 ${HOMEDIR}/houseofwhat
RUN chmod 444 ${HOMEDIR}/flag.txt


CMD socat -d TCP-LISTEN:3144,reuseaddr,fork EXEC:"./houseofwhat",raw,echo=0,setuid=issusr,pty,iexten=0