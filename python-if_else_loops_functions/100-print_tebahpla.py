#!/usr/bin/python3
for i in range(ord('Z'), ord('A') - 1, -1):
    print("{:c}".format(i + 32 if (ord('Z') - i) % 2 == 0 else i), end='')
