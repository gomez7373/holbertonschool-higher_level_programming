#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(i - 32 if (ord('z') - i) % 2 == 0 else i), end='')

