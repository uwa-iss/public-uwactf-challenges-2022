FROM python:3.9-slim-bullseye

RUN apt update && \
        apt install -y curl wget supervisor nginx gnupg unzip;

RUN mkdir -p /app
WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt
COPY app .
RUN chmod +x /app/api-start.sh
RUN chown -R www-data:www-data /app

COPY configs/supervisord.conf /etc/supervisord.conf
COPY configs/nginx.conf /etc/nginx/sites-available/default

EXPOSE 4244

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]