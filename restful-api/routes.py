#!/usr/bin/env python3

from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

# Your users dictionary
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password")}
}

# Secret key for token generation
SECRET_KEY = "your_secret_key_here"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify(error="Missing username or password"), 400
    if username not in users or not check_password_hash(users.get(username).get('password'), password):
        return jsonify(error="Invalid username or password"), 401
    # Generate JWT token
    token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
    return jsonify(access_token=token), 200

