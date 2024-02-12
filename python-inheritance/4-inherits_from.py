def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that
    inherited (directly or indirectly) from a_class; False otherwise.
    """
    if type(obj) == a_class:
        return True
    for base_class in type(obj).__bases__:
        if inherits_from(base_class, a_class):
            return True
    return False

# Test the function
if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
