#!/usr/bin/env python3
from flask import Flask, jsonify, request, Response
from typing import Dict, Union

app = Flask(__name__)

# Dictionary to store user data
users: Dict[str, Dict[str, Union[str, int]]] = {}


@app.route('/')
def home() -> str:
    """Route for the root URL."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data() -> Response:
    """Route to return a JSON response
    with a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status() -> str:
    """Route to return 'OK'."""
    return "OK"


@app.route('/users/<username>')
def get_user(username: str) -> Union[Dict[str, Union[str, int]], Response]:
    """Route to return the full object
    corresponding to the provided username."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user() -> Response:
    """Route to add a new user to the API."""
    data: Dict[str, Union[str, int]] = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 400  # Return an error if the username already exists
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 200


if __name__ == "__main__":
    app.run(debug=True)
