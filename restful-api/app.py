#!/usr/bin/env python3

from flask import Flask
from routes import app

if __name__ == '__main__':
    app.run(debug=True)
