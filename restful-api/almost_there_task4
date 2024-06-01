from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample user data stored in memory
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

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

# Route to check status
@app.route("/status")
def status():
    return "OK"

#---
# Endpoint to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    if request.is_json:
        user_data = request.get_json()
    else:
        user_data = request.args
    username = user_data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if not all(key in user_data for key in ["username", "name", "age", "city"]):
        return jsonify({"error": "Missing required fields"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": user_data.get('username'),
        "name": user_data.get('name'),
        "age": user_data.get('age'),
        "city": user_data.get('city')
    }

    return jsonify({"message": "User added", "user": users[username]}), 201



if __name__ == "__main__":
    app.run(debug=True)

