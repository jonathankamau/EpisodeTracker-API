#!/bin/bash
cho "Making Migrations..."
python /code/manage.py makemigrations
echo "Running Migrations..."
python /code/manage.py migrate
echo "Running App..."
gunicorn wsgi:application -b 0.0.0.0:8000
