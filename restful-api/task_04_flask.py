#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample user data stored in memory
users = {}

# Route for the root URL
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route to get all usernames
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

# Route to get user by username
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = data  # Assuming the data contains the full user object
    return jsonify({"message": "User added", "user": data}), 201

# Route to get the status of the API
@app.route("/status")
def status():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(debug=True)

