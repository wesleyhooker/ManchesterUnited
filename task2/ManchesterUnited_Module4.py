#!/usr/bin/env python3
"""
Reads in zip codes and prints out their bar values
"""
from __future__ import print_function
from urllib.request import urlopen
import ManchesterUnited_Module3


def module_four():
    """
    Prints out zipcode and its Bar Format
    :Params: NONE
    :Returns: NONE
    """
    #Open file from web
    test_file = urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt")
    #save webfile to an iterable list
    test_list = [line.decode("utf-8").strip("\n") for line in test_file]
    #print out the zip code and print its bar format
    for zip_code in test_list:
        print("Enter a zipcoe: {}".format(zip_code))
        ManchesterUnited_Module3.print_bar_code(zip_code)
        print("")

def main():
    """
    Test your module
    """
    module_four()


if __name__ == "__main__":
    main()
    exit(0)
