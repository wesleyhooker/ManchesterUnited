#!/usr/bin/env python3
"""

"""
from __future__ import print_function
from ManchesterUnited_Module1 import module_one
from urllib.request import urlopen


def module_two():
    test_file = []
    with urlopen('www.icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv') as the_file:
        for word in the_file:
            test_file.append(word.decode("utf-8"))
    print(test_file)

def main():
    """
    Test your module
    """
    module_two()


if __name__ == "__main__":
    main()
    exit(0)
