#!/bin/bash

cd /home/site/wwwroot

# Remove old copy and clone fresh
rm -rf PythonServerExample_tmp
git clone https://github.com/VraoNOVA/PythonServerExample.git PythonServerExample_tmp
rm -rf PythonServerExample
mv PythonServerExample_tmp PythonServerExample

cd /home/site/wwwroot/PythonServerExample

# Install dependencies
pip install django gunicorn

# Run migrations
export DJANGO_SETTINGS_MODULE=settings
python -m django migrate --settings=settings

# Start with Gunicorn (what Azure expects)
gunicorn --bind=0.0.0.0:8000 --timeout=600 wsgi:application
