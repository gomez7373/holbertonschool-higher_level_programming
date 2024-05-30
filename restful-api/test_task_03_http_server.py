#!/usr/bin/env/ pythone3

import unittest
import requests

class TestHTTPServer(unittest.TestCase):
    BASE_URL = "http://localhost:8000"

    def test_root_endpoint(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, this is a simple API!")

    def test_data_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/data")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data,
            {"name": "John", "age": 30,"city": "New York"})

    def test_status_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    def test_undefined_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/undefined")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, "Endpoint not found")

if __name__ == "__main__":
    unittest.main()
