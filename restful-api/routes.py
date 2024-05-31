#!/usr/bin/env python3

from flask import request

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify(error="Missing username or password"), 400
    if username not in users or not check_password_hash(users.get(username), password):
        return jsonify(error="Invalid username or password"), 401
    # Generate JWT token
    # Sample implementation
    return jsonify(access_token="your_generated_jwt_token")
