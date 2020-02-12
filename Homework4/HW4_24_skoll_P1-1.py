"""
Homework 4
>Problem 1 - P1

Author: Derrick Unger
Date: 2/07/20
CSC232 Winter 2020
"""

import numpy as np

# User Input
while True:
    try:
        n, a = input("\nInput n and a eg(1,2): ").split(",")
        n, a = eval(n), eval(a)

        if a == 0 or n == 0:
            print("a or n cannot be 0, log 0 is undefined, try again")
        if np.log(a) == 0:
            print("Denominator 0, try again")
        if n < 0 or a < 0:
            print("Cannot log negative number, try again")
        else:
            print("Valid input detected, calculating... \n")
            break

    except:
        print("\nError: Invalid input, retry\n")

numer = np.log(n)
denom = np.log(a)

answer = numer/denom
print("Result:", str.format('{0:.3f}', answer))
