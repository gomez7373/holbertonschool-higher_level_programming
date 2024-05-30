#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username missing"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    })

if __name__ == "__main__":
    app.run()

