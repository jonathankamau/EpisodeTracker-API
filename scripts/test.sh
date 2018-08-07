#!/bin/bash
echo "Making Migrations..."
python /application/manage.py makemigrations
echo "Running Migrations..."
python /application/manage.py migrate
echo "Running tests..."
python manage.py test
echo "Generating Covarage..."
coverage html
echo "Submitting Coverage to Coveralls..."
coveralls
