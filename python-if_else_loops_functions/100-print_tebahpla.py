#!/usr/bin/python3
output = ""
for i in range(ord('z'), ord('a') - 1, -1):
    output += chr(i) if (ord('z') - i) % 2 == 0 else chr(i - 32)
print(output, end='')

