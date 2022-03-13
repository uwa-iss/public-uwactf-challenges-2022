FROM ubuntu:bionic

ARG HOMEDIR="/chall"
WORKDIR "/chall"

RUN apt-get update; apt-get -y install socat gdb && rm -rf /var/lib/apt/*
RUN useradd --no-create-home --home-dir "${HOMEDIR}" issusr

RUN mkdir -p /chall
COPY outside ${HOMEDIR}/
COPY flag.txt ${HOMEDIR}/
RUN chmod 555 ${HOMEDIR}/outside
RUN chmod 444 ${HOMEDIR}/flag.txt

CMD socat -d TCP-LISTEN:3142,reuseaddr,fork EXEC:"./outside",raw,echo=0,setuid=issusr,pty,iexten=0