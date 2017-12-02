#!/bin/bash

#export FLASK_APP=main.py
#export FLASK_DEBUG=0
#python -m flask run
sleep 10
python3 main.py > web.log 2>&1
