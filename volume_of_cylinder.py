#!/usr/bin/env python3

# created by: Trinity Armstrong
# created on: September 2019
# This program calculates the volume of a cylinder in mm

import math


def main():
    # main function
    print("We will be calculating the volume of a cylinder. ")
    print("")

    # input
    radius = int(input("Enter the radius (mm): "))
    height = int(input("Enter the height (mm): "))

    # process
    volume = math.pi*radius**2*height
    print("")

    # output
    print("The volume is {}mm³".format(volume))


if __name__ == "__main__":
    main()
