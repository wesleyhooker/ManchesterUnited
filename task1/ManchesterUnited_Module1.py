#!/usr/bin/env python3
"""
This module tests to see which doors open or stay closed.
"""
from __future__ import print_function


def module_one(left_dash, right_dash, child_lock, master_unlock, left_inside,
               left_outside, right_inside, right_outside, gear_shift):
    """
    This module test to see which doors open or stay closed
    Param: left_dash, right_dash, child_lock, master_unlock, left_inside,
               left_outside, right_inside, right_outside, gear_shift
    Returns: string indicating the position of the doors
    """
    if gear_shift != "P":
        print("Both doors stay closed.")
        return
    elif master_unlock == 0:
        print("Both doors stay closed.")
        return
    if child_lock == 1:
        left_inside = 0
        right_inside = 0

    # decide which doors open
    if 1 in (left_inside, left_outside, left_dash):
        left_door_open = True
    else:
        left_door_open = False

    if 1 in (right_inside, right_outside, right_dash):
        right_door_open = True
    else:
        right_door_open = False

    if left_door_open and right_door_open:
        print("Both doors open")
        return
    if left_door_open:
        print("Left doors open")
        return
    if right_door_open:
        print("Right doors open")
        return


def main():
    """
    Test your module
    """
    module_one(0, 1, 0, 1, 0, 1, 0, 0, "P")


if __name__ == "__main__":
    main()
    exit(0)
