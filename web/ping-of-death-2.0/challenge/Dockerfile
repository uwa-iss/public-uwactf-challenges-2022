FROM debian:buster-slim

# Install system packages
RUN apt-get update && apt-get install -y supervisor nginx lsb-release curl wget

# Add repos
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list

# Install PHP dependencies and ping
RUN apt update && apt install -y php7.4-fpm iputils-ping


# Configure php-fpm and nginx
RUN mkdir -p /bin/challenge && \
    cp /bin/cat /bin/challenge/cat && \
    cp /bin/ls /bin/challenge/ls && \
    cp /usr/bin/id /bin/challenge/id && \
    cp /usr/bin/whoami /bin/challenge/whoami && \
    # cp /usr/bin/cp /bin/challenge/cp && \
    # cp /usr/bin/sleep /bin/challenge/sleep && \
    cp /usr/bin/curl /bin/challenge/curl && \
    cp /usr/bin/wget /bin/challenge/wget && \
    ln -s /bin/ping /bin/challenge/ping 

COPY config/fpm.conf /etc/php/7.4/fpm/php-fpm.conf
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/nginx.conf /etc/nginx/nginx.conf

# Copy challenge files
COPY src /var/www/html

# Copy flag
COPY flag /flag
RUN chmod 444 /flag

# Setup permissions
RUN chown -R www-data:www-data /var/www/html/assets
RUN chown -R www-data:www-data /var/www/html/images

RUN chmod -R 550 /var/www/html/assets
RUN chmod -R 550 /var/www/html/images
RUN chmod -R +r /var/www/html/
RUN echo "echo Gotchya ya cheeky scrub trying to run rm -rf / on my challenge!" > /bin/rm
RUN echo "echo We are gonna DDoS your IP for trying to hack this server!" > /bin/chmod
RUN echo "echo My ping of death is like the SOL cannon from Akira. Watch yourself!" > /bin/rmdir

# Expose the port nginx is listening on
EXPOSE 1004

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
