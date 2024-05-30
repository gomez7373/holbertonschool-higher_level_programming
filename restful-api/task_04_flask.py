#!/usr/bin/pythone3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
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
    if 'username' not in data:
        return "Username missing", 400
    username = data['username']
    if username in users:
        return "Username already exists", 400
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    })

if __name__ == "__main__":
    app.run(debug=True)
