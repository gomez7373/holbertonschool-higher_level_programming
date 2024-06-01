#!/bin/bash

# Kill any process using port 5000
fuser -k 5000/tcp

# Run Flask app in the background
python3 task_04_flask.py &

# Wait for the Flask app to start
sleep 2

# Run the tests
python3 -m unittest test_04_flask.py

# Kill the Flask app process
fuser -k 5000/tcp

