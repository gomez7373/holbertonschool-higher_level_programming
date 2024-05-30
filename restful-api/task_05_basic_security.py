#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash  # Make sure to import these functions

app = Flask(__name__)
auth = HTTPBasicAuth()

# Replace 'super-secret' with 'gomez_key' for token generation and validation
app.config['JWT_SECRET_KEY'] = 'gomez_key'

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpassword"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username).get('password'), password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
