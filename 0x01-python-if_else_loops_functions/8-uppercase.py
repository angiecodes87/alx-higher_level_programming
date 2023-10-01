#!/usr/bin/python3

def uppercase(input_str):
    for char in input_str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - (ord('a') - ord('A')))
        else:
            uppercase_char = char
        print(uppercase_char, end="")
    print()  # Print a newline at the end
