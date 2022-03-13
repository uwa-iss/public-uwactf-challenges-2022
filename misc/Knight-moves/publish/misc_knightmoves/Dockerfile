FROM python:3.9-slim

WORKDIR "/challenge"

RUN apt-get update
RUN apt-get -y install socat && rm -rf /var/lib/apt/*

RUN mkdir -p /challenge

COPY challenge.py .

RUN chmod +x challenge.py

CMD socat -d TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 challenge.py"