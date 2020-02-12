"""
Homework 4
>Problem 1 - P3

Author: Derrick Unger
Date: 2/07/20
CSC232 Winter 2020
"""
import numpy as np

L = [12, 14.5, 3.14159]

# User Input
while True:
    try:
        userInput = input("\nInput a value to add to list: ")

        if userInput.upper() == "EXIT":
            print("\nExit detected, quitting...\n")
            break

        term = eval(userInput)
        L.append(term)

    except:
        print("\nError: Invalid input, retry\n")

L.sort()  # Ascending Order
print(L)
L.sort(reverse=True)  # Descending Order
print(L)
print("AVG: ", str.format('{0:.3f}', np.average(L)))  # Average
print("STD DEV: ", str.format('{0:.3f}', np.std(L)))  # Average
