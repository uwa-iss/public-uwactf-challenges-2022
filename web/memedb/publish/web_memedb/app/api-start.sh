#!/bin/bash

python3 /app/app.py --init;
gunicorn --bind unix:/tmp/webapi.sock --workers 3 -m 007 wsgi:app;