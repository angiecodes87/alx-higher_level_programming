#!/usr/bin/python3
import hidden_4

def print_module_names():
    """Print all names defined by the hidden_4 module."""
    names = [name for name in dir(hidden_4) if not name.startswith('__')]
    for name in names:
    print(name)

if __name__ == "__main__":
    print_module_names()
