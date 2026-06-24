#!/bin/bash

cd /home/site/wwwroot

# Clone or pull latest code
if [ -d "PythonServerExample" ]; then
    cd PythonServerExample
    git pull
else
    git clone https://github.com/VraoNOVA/PythonServerExample.git
    cd PythonServerExample
fi

# Install dependencies
pip install django

# Run migrations
python -m django migrate --settings=settings

# Start the server
python -m django runserver 0.0.0.0:8000 --settings=settings
