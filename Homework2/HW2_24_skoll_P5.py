"""
Homework 2
>Problem 5

Author: Derrick Unger
Date: 1/24/20
CSC232 Winter 2020
"""

import numpy as np

print("\n=======================================")
print("     Paper Towel Problem\n")


while True:
    try:
        r1 = eval(input("Enter radius size in mm: "))
        r2 = np.sqrt(.5*r1**2)
        percentR = (r2/r1)*100
        print(str.format('{0:.2f}', percentR), "%")
        break

    except:
        print("\nError: Invalid value, try again\n")

print("=======================================\n")
