#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns the key with the biggest integer value."""
    if not a_dictionary:
        return None

    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key
