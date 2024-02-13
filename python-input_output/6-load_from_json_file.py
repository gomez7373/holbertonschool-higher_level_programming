#!/usr/bin/python3

def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object represented by the JSON data.

    """
    import json

    with open(filename, 'r') as file:
        return json.load(file)
