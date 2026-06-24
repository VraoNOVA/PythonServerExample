#!/bin/bash

cd /home/site/wwwroot

# Remove old copy and clone fresh
rm -rf PythonServerExample_tmp
git clone https://github.com/VraoNOVA/PythonServerExample.git PythonServerExample_tmp
rm -rf PythonServerExample
mv PythonServerExample_tmp PythonServerExample

# Start the server
cd /home/site/wwwroot/PythonServerExample && python -m django runserver 0.0.0.0:8000 --settings=settings
