#!/usr/bin/env python3

import unittest
import requests

class TestHTTPServer(unittest.TestCase):

    def test_root_endpoint(self):
        response = requests.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Hello, this is a simple API!')

    def test_data_endpoint(self):
        response = requests.get('http://localhost:8000/data')
        self.assertEqual(response.status_code, 200)
        # Add assertions to check the content of the response

    def test_status_endpoint(self):
        response = requests.get('http://localhost:8000/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'OK')

    def test_undefined_endpoint(self):
        response = requests.get('http://localhost:8000/undefined')
        self.assertEqual(response.status_code, 404)

