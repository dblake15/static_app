from flask import Flask, flash, url_for, render_template, request, Response, redirect, session
from markupsafe import escape
import sys
import json
import logging
import re
# Create our global variable 'app'
app = Flask(__name__) 
# App routes are used to handle browser requests at different endpoints in our project
@app.route('/')
def home():
    host_str = request.host
    ret = ""
    for c in host_str:
        if c == ":":
            break
        else:
            ret += c

    return "'" + ret + "'"

if __name__ == '__main__':
    app.debug = True
    app.run(use_reloader=True, host='0.0.0.0', port=8080)