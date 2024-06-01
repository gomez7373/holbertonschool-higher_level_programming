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

# Route to add a new user
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    else:
        users[username] = data  # Assuming the data contains the full user object
        return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)

