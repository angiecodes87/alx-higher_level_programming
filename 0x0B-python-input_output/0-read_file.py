#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print its content to stdout.

    Args:
        filename (str): The name of the file to be read. (default: "")

    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")


# Example usage:
if __name__ == "__main__":
    read_file("my_file_0.txt")
