#!/usr/bin/python3


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.

    """
    import json
    return json.dumps(my_obj)
