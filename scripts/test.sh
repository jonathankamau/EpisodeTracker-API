#!/bin/bash
echo "Running tests..."
coverage run -m pytest -v
echo "Generating Covarage..."
coverage html
echo "Submitting Coverage to Coveralls..."
coveralls