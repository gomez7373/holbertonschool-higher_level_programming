def islower(c):
    # Check if the ASCII value of the character is in the range of lowercase letters
    return 97 <= ord(c) <= 122

# Test cases
print(islower('a'))  # True
print(islower('H'))  # False
print(islower('A'))  # False
print(islower('3'))  # False
print(islower('g'))  # True
