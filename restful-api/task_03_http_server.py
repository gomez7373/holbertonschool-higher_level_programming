#!/usr/bin/python3
"""Module for a simple server"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Simple HTTP request handler with routing dictionary"""
    
    def do_GET(self):
        routes = {
            '/': self.handle_root,
            '/data': self.handle_data,
            '/info': self.handle_info,
            '/status': self.handle_status
        }
        
        handler = routes.get(self.path, self.handle_404)
        handler()

    def handle_root(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def handle_data(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = {"name": "John", "age": 30, "city": "New York"}
        self.wfile.write(json.dumps(data).encode())

    def handle_info(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = {"version": "1.0", "description": "A simple API built with http.server"}
        self.wfile.write(json.dumps(data).encode())

    def handle_status(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK")

    def handle_404(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"404 Not Found")


def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Starting server...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()

