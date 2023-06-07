#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            diff = ord('a') - ord('A')
            upper_char = chr(ord(char) - diff)
        else:
            upper_char = char
    print("{}".format(upper_char), end='')


print()
