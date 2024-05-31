import unittest
import requests

class TestJWTAuthentication(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:5000"
        self.login_url = f"{self.base_url}/login"

    def test_invalid_credentials(self):
        response = requests.post(
            self.login_url,
            json={"username": "user1", "password": "wrongpassword"}
        )
        self.assertEqual(response.status_code, 401)

    def test_valid_credentials(self):
        response = requests.post(
            self.login_url,
            json={"username": "user1", "password": "password"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())

if __name__ == "__main__":
    unittest.main()

