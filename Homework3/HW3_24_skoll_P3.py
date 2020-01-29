"""
Homework 3
>Problem 3

Author: Derrick Unger
Date: 1/31/20
CSC232 Winter 2020
"""
import numpy as np

while True:
    try:
        a, b, c = input("\nInput coefficients a, b, and c: ").split(" ")

        if a.upper() == "EXIT" or b.upper() == "EXIT" or c.upper() == "EXIT":
            print("\nExit detected, quitting...\n")
            break

        a = eval(a)
        b = eval(b)
        c = eval(c)

        if a == 0:
            print("\nInvalid quadratic, 'a' cannot be zero, retry\n")

        else:
            if (b**2) - 4*a*c < 0:
                x1 = (-b + np.sqrt(complex((b**2) - 4*a*c)))/(2*a)
                x2 = (-b - np.sqrt(complex((b**2) - 4*a*c)))/(2*a)
            else:
                x1 = (-b + np.sqrt((b**2) - 4*a*c))/(2*a)
                x2 = (-b - np.sqrt((b**2) - 4*a*c))/(2*a)
            x1 = str.format('{0:.2f}', x1)
            x2 = str.format('{0:.2f}', x2)
            print("\nRoots: ", x1, " ", x2)
            print("To quit, type exit in 1 of the 3 inputs (eg 0 exit 0)")
    except:
        print("\nError: Invalid input, retry\n")
