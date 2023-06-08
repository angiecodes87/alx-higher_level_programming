#!/usr/bin/python3

import sys


def main():
    """Print the addition of all arguments."""
    total = sum(int(arg) for arg in sys.argv[1:])
    print(total)


if __name__ == "__main__":
    main()
