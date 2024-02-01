#!/usr/bin/pythone3

def update_dictionary(a_dictionary, key, value):

    return (a_dictionary.update({key: value}) or a_dictionary)
