FROM ubuntu:bionic

ARG HOMEDIR="/chall"
WORKDIR "/chall"

RUN apt-get update; apt-get -y install socat gdb && rm -rf /var/lib/apt/*
RUN useradd --no-create-home --home-dir "${HOMEDIR}" issusr

RUN mkdir -p /chall
COPY babyheap ${HOMEDIR}/
COPY flag.txt ${HOMEDIR}/
RUN chmod 555 ${HOMEDIR}/babyheap
RUN chmod 444 ${HOMEDIR}/flag.txt

CMD socat -d TCP-LISTEN:3141,reuseaddr,fork EXEC:"./babyheap",raw,echo=0,setuid=issusr,pty,iexten=0
