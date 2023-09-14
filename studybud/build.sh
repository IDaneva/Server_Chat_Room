#!/usr/bin/env bash
# exit on error
set -o errexit

cd studybud
pip install django-cors-headers
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate