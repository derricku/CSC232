"""
Homework 5
>Problem 3

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""

import numpy as np
np.set_printoptions(formatter={'float_kind': lambda value: format(value, '8.3f'),
                               'int_kind': lambda value: format(value, '10d')})

print("\nINSTRUCTIONS")
print("-"*len("INSTRUCTIONS"))
print("Input arrays by value and by row i.e for ([1,2],[3,4]),"
      " input 1,2,3,4 all separated by commas and on one line.\n")

while True:
    try:
        # 3x2 Array
        print("3x2 Array Builder (only first 6 inputs accpeted)...")
        a = list(map(eval, input("\nEnter values : ").split(",")))[:6]
        array1 = np.reshape(np.array(a), (3, 2))

        # 2x1 Array
        print("2x1 Array Builder (only first 2 inputs accepted)...")
        b = list(map(eval, input("\nEnter values : ").split(",")))[:2]
        array2 = np.reshape(np.array(b), (2, 1))

        break

    except:
        print("\nError: Invalid input, retry\n")

# Dot Product
print("Array 1: \n", array1)
print("Array 2: \n", array2)
print("Dot Product: \n", np.dot(array1, array2))
