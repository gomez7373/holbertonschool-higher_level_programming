#!/usr/bin/env python3
"""
RESTful API with basic and JWT token authentication.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, \
    create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configure basic authentication
auth = HTTPBasicAuth()

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

# Users data (replace with your actual users)
users = {
    "admin": {
        "username": "admin",
        "password": generate_password_hash("gomez_key"),
        "role": "admin"
    }
}

# Custom error handlers for JWT
@jwt.unauthorized_loader
def handle_unauthorized_error():
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error():
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error():
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error():
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error():
    return jsonify({"error": "Fresh token required"}), 401

# Basic authentication callback
@auth.verify_password
def verify_password(username, password):
    """
    Verify the password for the given username.
    """
    if username in users and \
            check_password_hash(users[username]['password'], password):
        return username

# Protected route with basic authentication
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Returns a message if the user provides valid basic authentication credentials.
    """
    return "Basic Auth: Access Granted"

# Login route for JWT token
@app.route('/login', methods=['POST'])
def login():
    """
    Accepts JSON payload with username and password.
    Returns a JWT token if credentials are valid.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    if username not in users or \
            not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

# Protected route with JWT authentication
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Returns a message if the user provides a valid JWT token.
    """
    return "JWT Auth: Access Granted"

# Role-based protected route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Returns a message if the user is an admin, otherwise returns an error message.
    """
    current_user = get_jwt_identity()
    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

