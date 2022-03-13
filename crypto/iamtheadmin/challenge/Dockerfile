FROM ubuntu:20.04

ARG HOMEDIR="/chall"
WORKDIR "/chall"

RUN apt-get update && apt-get -y install socat python3-pip && rm -rf /var/lib/apt/*
RUN useradd --no-create-home --home-dir "${HOMEDIR}" issusr
RUN pip3 install pycryptodome

RUN mkdir -p /chall
COPY app.py ${HOMEDIR}/app.py
COPY flag.py ${HOMEDIR}/flag.py
RUN chmod 555 ${HOMEDIR}/app.py
RUN chmod 555 ${HOMEDIR}/flag.py

EXPOSE 4246
CMD socat -d TCP-LISTEN:4246,reuseaddr,fork EXEC:"/chall/app.py",raw,echo=0,setuid=issusr,pty,iexten=0