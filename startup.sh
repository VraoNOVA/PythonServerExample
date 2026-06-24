#!/bin/bash

cd /home/site/wwwroot

# Remove old copy and clone fresh
rm -rf PythonServerExample
git clone https://github.com/VraoNOVA/PythonServerExample.git

# Start the server
cd /home/site/wwwroot/PythonServerExample && python -m django runserver 0.0.0.0:8000 --settings=settings
