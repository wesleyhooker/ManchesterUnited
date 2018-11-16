#!/usr/bin/env python3
"""

"""
from __future__ import print_function
from ManchesterUnited_Module1 import module_one
from urllib.request import urlopen


def module_two():
    """

    """
    test_file = urlopen('http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv')
    test_list = [line.decode('utf-8').strip('\n') for line in test_file]
    del test_list[0]

    count = 1
    for values in test_list:
        print("Reading Record {}:".format(count))
        values_list = values.split(", ")
        del values_list[0]
        print(*values_list)
        module_one(*values_list)
        print()
        count += 1
       # module_one(value_list)

def main():
    """
    Test your module
    """
    module_two()


if __name__ == "__main__":
    main()
    exit(0)
