#!/usr/bin/python3
"""
Module for a simple Flask API.
"""

from typing import Dict, Union  # Standard library import should come first
from flask import Flask, jsonify, request, Response

# Third-party library import, line above.

app = Flask(__name__)

# Dictionary to store user data
users: Dict[str, Dict[str, Union[str, int]]] = {}


@app.route("/")
def home() -> str | Response:
    """Route for the root URL."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data() -> str | Response:
    """Route to return a JSON response
    with a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status() -> str | Response:
    """Route to return 'OK'."""
    return "OK"


@app.route("/users/<username>")
def get_user(username: str) -> str | Response:
    """Route to return the full object
    corresponding to the provided username."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user() -> str | Response:
    """Route to add a new user to the API."""
    data: Dict[str, Union[str, int]] = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 200


if __name__ == "__main__":
    app.run(debug=True)
