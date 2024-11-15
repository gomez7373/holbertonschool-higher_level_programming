#!/usr/bin/python3
import sys
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    print(f'{a} {operator} {b} = {result}')
