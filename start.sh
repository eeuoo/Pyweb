#!/bin/sh

nodemon --exec /Library/Frameworks/Python.framework/Versions/3.7/bin/python3 start_helloflask.py -w helloflask/__init__.py -w helloflask/templates/*.html
