#!/usr/bin/env python3
from flask import Flask, url_for

app = Flask(__name__)
app.config['SERVER_NAME']='server:80'

@app.route('/')
def entry_point():
    return 'Hello World! ' + url_for('index', _external=True)

@app.route('/index')
def index():
    return 'Index'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


