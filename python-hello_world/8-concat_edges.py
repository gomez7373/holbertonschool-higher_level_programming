#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = f"{str[39:-64]}{str[106:-17]}{str[:-123]}"
print(str)
