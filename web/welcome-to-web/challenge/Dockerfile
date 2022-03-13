FROM debian:buster-slim

# Install system packeges
RUN apt-get update && apt-get install -y supervisor nginx lsb-release curl wget build-essential

# Add repos
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list

# Install PHP dependencies and ping
RUN apt update && apt install -y php7.4-fpm

COPY config/fpm.conf /etc/php/7.4/fpm/php-fpm.conf
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/nginx.conf /etc/nginx/nginx.conf

RUN apt install -y git cron

COPY config/wipe-logs-cron /etc/cron.d/wipe-logs-cron
COPY config/clearlogs.sh /root/clearlogs.sh

RUN chmod +x /root/clearlogs.sh && \
        chmod 644 /etc/cron.d/wipe-logs-cron && \
        crontab /etc/cron.d/wipe-logs-cron;

# Copy challenge files
COPY src /var/www/html

RUN chmod -R 555 /var/www/html/

RUN echo "ISS{lF1_w1ll_c4v53_tH15_w3B_2_d13!1!}" > /flag

RUN useradd -m ghostccamm && \
        echo "ISS{p01s0n0v5_l0G5_c4n_r35vLt_1n_rC3!one}" > /home/ghostccamm/flag && \
        chown ghostccamm:ghostccamm /home/ghostccamm/flag && \
        chmod -R 770 /home/ghostccamm;

COPY getfinalflag/getfinalflag.c /tmp/getfinalflag.c
RUN gcc -o /usr/bin/getfinalflag /tmp/getfinalflag.c && \
    chown -R ghostccamm:ghostccamm /usr/bin/getfinalflag && \
    chmod u+s /usr/bin/getfinalflag

RUN cd /var/www/html/topsecretconstruction/v1 && \
        git config --global user.email "ghostccamm@hickityhack.com" && \
        git config --global user.name "ghostccamm" && \
        git init && \
        echo "ISS{3xp05eD_g1T_r3P0!1!!one!}" > secret.txt && \
        git add -A && \
        git commit -m 'initial commit' && \
        rm secret.txt && \
        git add -A && \
        git commit -m 'remove secret.txt'

# Expose the port nginx is listening on
EXPOSE 4245

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
