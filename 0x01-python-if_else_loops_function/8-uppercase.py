#!/usr/bin/python3

def uppercase(string):
	uppercase_str = ""
	for char in string:
		if ord(char) >= 97 and ord(char) <= 122:
			char = chr(ord(char) - 32)
		uppercase_str += char
	print(uppercase_str)

