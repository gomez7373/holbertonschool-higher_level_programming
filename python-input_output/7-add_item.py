#!/usr/bin/python3


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Get the existing items from the file if it exists
try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

# Append the new items from the command line arguments
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, "add_item.json")
