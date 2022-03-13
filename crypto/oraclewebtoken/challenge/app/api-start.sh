#!/bin/bash

gunicorn --bind unix:/tmp/webapi.sock --workers 3 -m 007 wsgi:app;