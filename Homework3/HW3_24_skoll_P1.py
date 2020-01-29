"""
Homework 3
>Problem 1
Author: Derrick Unger
Date: 1/31/20
CSC232 Winter 2020
"""

import numpy as np
code = 1
print("\n=============================================")

while code == 1:
    try:
        x = int(input("Enter a fairly large integer: "))
        print("{:.2e}".format(x))
        if x == 0:
            code = 0

    except:
        print("Invalid integer, please try again")
print("=============================================\n")
