#!/bin/bash

#export FLASK_APP=main.py
#export FLASK_DEBUG=0
#python -m flask run
sleep 20
#python3 main.py > web.log 2>&1
gunicorn --bind 0.0.0.0:5000 wsgi:app --log-file web.log --log-level info --workers 3 --timeout 120

