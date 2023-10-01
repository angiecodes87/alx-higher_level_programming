#!/usr/bin/python3

def uppercase(input_str):
    for char in input_str:
        ascii_value = ord(char)
        if ord('a') <= ascii_value <= ord('z'):
            uppercase_char = chr(ascii_value - (ord('a') - ord('A')))
        else:
            uppercase_char = char
        print(uppercase_char, end="")
    print()  # Print a newline at the end
