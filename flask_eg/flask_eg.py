"""Main module."""

__author__ = """Philip Kershaw"""
__contact__ = 'philip.kershaw@stfc.ac.uk'
__copyright__ = "Copyright 2022 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return '<h1>Hello World</h1>'

@app.route('/goodbye')
def goodbye_world():
   return '<h1>Good-bye!</h1>'


if __name__ == '__main__':
   app.run()