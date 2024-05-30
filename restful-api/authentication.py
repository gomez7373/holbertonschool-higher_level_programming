#!/usr/bin/env python3
from flask_jwt_extended import create_access_token

def authenticate(username, password):
    # Dummy authentication function, replace with actual authentication logic
    if username == "user1" and password == "password":
        return {"username": "user1", "role": "user"}

def login(username, password):
    # Dummy login function, replace with actual authentication logic
    user = authenticate(username, password)
    if user:
        access_token = create_access_token(identity=user["username"])
        return {"access_token": access_token}
    else:
        return {"error": "Invalid username or password"}, 401
