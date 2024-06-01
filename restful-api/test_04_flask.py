import unittest
import json
from task_04_flask import app, users

class FlaskApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Reset the users dictionary before each test
        users.clear()

    def test_home_route(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, b"Welcome to the Flask API!")

    def test_data_route_no_users(self):
        result = self.app.get('/data')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), [])

    def test_add_user(self):
        result = self.app.post('/add_user', json={"username": "alice", "name": "Alice", "age": 25, "city": "Paris"})
        self.assertEqual(result.status_code, 201)
        self.assertEqual(json.loads(result.data)['user']['username'], "alice")

    def test_data_route_with_user(self):
        self.app.post('/add_user', json={"username": "alice", "name": "Alice", "age": 25, "city": "Paris"})
        result = self.app.get('/data')
        self.assertEqual(result.status_code, 200)
        self.assertIn("alice", json.loads(result.data))

    def test_get_user(self):
        self.app.post('/add_user', json={"username": "alice", "name": "Alice", "age": 25, "city": "Paris"})
        result = self.app.get('/users/alice')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data)['name'], "Alice")

    def test_get_nonexistent_user(self):
        result = self.app.get('/users/doesnotexist')
        self.assertEqual(result.status_code, 404)
        self.assertEqual(json.loads(result.data)['error'], "User not found")

    def test_status_route(self):
        result = self.app.get('/status')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data)['status'], "OK")

    def test_add_user_without_username(self):
        result = self.app.post('/add_user', json={"name": "NoName", "age": 20, "city": "Unknown"})
        self.assertEqual(result.status_code, 400)
        self.assertEqual(json.loads(result.data)['error'], "Username is required")

    def test_add_user_with_duplicate_username(self):
        self.app.post('/add_user', json={"username": "alice", "name": "Alice", "age": 25, "city": "Paris"})
        result = self.app.post('/add_user', json={"username": "alice", "name": "Alice", "age": 25, "city": "Paris"})
        self.assertEqual(result.status_code, 400)
        self.assertEqual(json.loads(result.data)['error'], "User already exists")

if __name__ == '__main__':
    unittest.main()

