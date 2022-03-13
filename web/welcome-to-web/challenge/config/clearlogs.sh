#!/bin/bash

/bin/echo "" > /var/log/nginx/access.log;
/bin/echo "" > /var/log/nginx/error.log;
# Prepopulate access.log so it isn't empty.
curl -m 20 -sf http://localhost:4245/;