#!/usr/bin/python3

def uniq_add(my_list=[]):

    result_set = set()
    result_sum = 0

    for x in my_list:
        if x not in result_set:
            result_sum += x
            result_set.add(x)
        return result_sum
