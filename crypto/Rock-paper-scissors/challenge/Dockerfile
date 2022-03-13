FROM python:3.9-slim

WORKDIR "/challenge"

RUN apt-get update
RUN apt-get -y install socat && rm -rf /var/lib/apt/*

RUN mkdir -p /challenge

COPY . .

RUN chmod +x challenge.py

CMD python3 challenge.py