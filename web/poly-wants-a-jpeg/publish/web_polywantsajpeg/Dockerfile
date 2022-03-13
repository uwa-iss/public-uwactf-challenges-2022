FROM python:3.9-slim-bullseye

RUN apt update && \
        apt install -y curl wget supervisor nginx gnupg unzip && \
        wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
        echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
        apt update && \
        apt install -y google-chrome-stable --no-install-recommends && \
        CHROME_VERSION=$(google-chrome --version | cut -d ' ' -f 3 | tr -d '\n') && \
        wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROME_VERSION}/chromedriver_linux64.zip && \
        unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN mkdir -p /app
WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt
COPY app .
RUN chmod +x /app/api-start.sh
RUN chown -R www-data:www-data /app

COPY configs/supervisord.conf /etc/supervisord.conf
COPY configs/nginx.conf /etc/nginx/sites-available/default

EXPOSE 4243

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]