#!/usr/bin/env python3
"""
Program to print the zipcode into bar format
"""
from __future__ import print_function


def print_digit(digit):
    """
    Finds the checksum
    :Params: digit: the zipcode passed in (or digit)
    :Returns: The Checksum of the zipcode in int format
    """
    #Variables
    sum_digits = 0
    digit = int(digit)
    #Finds the sum of the zipCode (digit)
    while digit:
        sum_digits += digit % 10
        digit //= 10
    #Finds the number to add to get a multiple of 10
    check_digit = 10 - (sum_digits % 10)
    if check_digit == 10:
        check_digit = 0
    #Translate check_digit to value
    if check_digit == 1:
        check_digit = "00011"
    elif check_digit == 2:
        check_digit = "00101"
    elif check_digit == 3:
        check_digit = "00110"
    elif check_digit == 4:
        check_digit = "01001"
    elif check_digit == 5:
        check_digit = "01010"
    elif check_digit == 6:
        check_digit = "01100"
    elif check_digit == 7:
        check_digit = "10001"
    elif check_digit == 8:
        check_digit = "10010"
    elif check_digit == 9:
        check_digit = "10100"
    elif check_digit == 0:
        check_digit = "11000"
    return check_digit


def print_bar_code(zip_code):
    """
    Prints the zipcode in bar format
    :Params: zip_code: the zipcode given
    :Returns: Nothing
    """
    #Check for errors
    if not zip_code.isdigit():
        print("Error: Zip code is not all numeric")
        return
    if len(zip_code) != 5:
        print("Error: Zip code is not 5 digits")
        return
    #variables
    string_zip_code = zip_code
    translation = ""
    check_digit = print_digit(zip_code)
    #Translate zip to values
    for i in string_zip_code:
        if i == "1":
            translation += "00011"
        elif i == "2":
            translation += "00101"
        elif i == "3":
            translation += "00110"
        elif i == "4":
            translation += "01001"
        elif i == "5":
            translation += "01010"
        elif i == "6":
            translation += "01100"
        elif i == "7":
            translation += "10001"
        elif i == "8":
            translation += "10010"
        elif i == "9":
            translation += "10100"
        elif i == "0":
            translation += "11000"
    #Append check_digit to end of translation
    translation += check_digit
    #Print in bar format
    print("|", end="")
    for number in translation:
        if number == "0":
            print(":", end="")
        if number == "1":
            print("|", end="")
    print("|")


def main():
    """
    Test your module
    """
    print_bar_code("123")


if __name__ == "__main__":
    main()
    exit(0)
