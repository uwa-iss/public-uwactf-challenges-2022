#!/bin/bash

python3 /app/app.py --init;
# Start poly bot
python3 /app/poly.py &
gunicorn --bind unix:/tmp/webapi.sock --workers 3 -m 007 wsgi:app;