"""
Homework 5
>Problem 3

Author: Derrick Unger
Date: 2/07/20
CSC232 Winter 2020
"""

import numpy as np

while True:
    try:
        print("This array must be input as: 1,2,3,4,5,6 where 1,2 is the 1st" \
              " row and 3,4 is the second row, and 5,6 is the third row")
        a, b, c, d, e, f = input("\n Enter a 3x2 array: ").split(",")
        
        array1 = np.array(([eval(a),eval(b)],[eval(c),eval(d)],[eval(e),eval(f)]))
        
        print("This array must be input as:  1,2")
        g, h = input("\n Enter a 2x1 array: ").split(",")
        
        array2 = np.array(([eval(g),eval(h)]))

        break

    except ZeroDivisionError:
        print("\nError: Invalid input, retry\n")
        


