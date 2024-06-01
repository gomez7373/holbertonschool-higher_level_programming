from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()  # Define the HTTPBasicAuth object
jwt = JWTManager(app)

users = {
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("gomez_key"),
        "role": "admin"
    },
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    }
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/jwt-protected')
@jwt_required
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

