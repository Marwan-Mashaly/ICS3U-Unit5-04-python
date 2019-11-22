#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program tells user the month afte typing the number

import math


def volume_calc(rad, int_h):
    # This function calculates the volume of a cylinder

    volume = math.pi*pow(rad, 2)*int_h
    return volume


def main():
    # This function takes input from the user and calls other functions
    height = input("Enter height of the cylinder (mm): ")
    radius = input("Enter radius of the cylinder (mm): ")
    print("")
    try:
        height_check = int(height)
        radius_check = int(radius)
        solution = volume_calc(int_h=height_check, rad=radius_check)
        print("the solution is : {0:.2f} (mm^2)".format(solution))
    except Exception:
        print("Invalid Integer ")
        print("")


if __name__ == "__main__":
    main()
