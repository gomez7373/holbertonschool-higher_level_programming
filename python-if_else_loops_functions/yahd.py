#!/usr/bin/python3

def my_sum(a, b):
    return a + b

def call_sum():
    calling_sum = my_sum(10, 10)
    return calling_sum

result = my_sum(2, 2)
call = call_sum()

print(f"Your result is {result}")
print(f"Your calling sum result is {call}")

