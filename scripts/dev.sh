#!/bin/bash
python /code/manage.py migrate
gunicorn wsgi:application -b 0.0.0.0:8000
