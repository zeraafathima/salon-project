#!/bin/bash

# Exit immediately if any command fails
set -o errexit  

pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput