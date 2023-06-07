#!/usr/bin/pyt
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            diff = ord('A') - ord('a')
            upper_char = chr(ord(char) + diff)
        else:
            upper_char = char
    print("{}".format(upper_char), end='')


print()
