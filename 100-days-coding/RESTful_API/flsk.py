#!/usr/bin/python3

from flask import Flask

app = Flask('flaskapp')

@app.route('/home')
def home():
    return 'welcome home'

if __name__ == '__main__':
    app.run()
