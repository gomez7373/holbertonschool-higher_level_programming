#!/usr/bin/env python3

import requests
import csv

def fetch_and_print_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    # Print the status code of the response
    print(f"Status Code: {response.status_code}")
    
    # If the request was successful, parse the data into a JSON object
    if response.status_code == 200:
        posts = response.json()
        
        # Iterate through the JSON data and print the titles of all posts
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    # If the request was successful, parse the data into a JSON object
    if response.status_code == 200:
        posts = response.json()
        
        # Structure the data into a list of dictionaries
        post_data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]
        
        # Write the data into a CSV file
        with open("posts.csv", mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(post_data)

# The following part is for testing the functions
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()

