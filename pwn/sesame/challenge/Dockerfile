FROM i386/ubuntu:bionic

ARG HOMEDIR="/chall"
WORKDIR "/chall"

RUN apt-get update; apt-get -y install socat gdb && rm -rf /var/lib/apt/*
RUN useradd --no-create-home --home-dir "${HOMEDIR}" issusr

RUN mkdir -p /chall
COPY sesame ${HOMEDIR}/
COPY flag.txt ${HOMEDIR}/
RUN chmod 555 ${HOMEDIR}/sesame
RUN chmod 444 ${HOMEDIR}/flag.txt

CMD socat -d TCP-LISTEN:3143,reuseaddr,fork EXEC:"./sesame",raw,echo=0,setuid=issusr,pty,iexten=0