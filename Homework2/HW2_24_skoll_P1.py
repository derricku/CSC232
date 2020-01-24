"""
Homework 2
>Problem 1

Author: Derrick Unger
Date: 1/24/20
CSC232 Winter 2020
"""

import numpy as np


while True:
    try:
        print("\n=============================================")
        x = eval(input("Please enter a numerical value: "))
        print("Thank you for entering a valid number!")
        a = np.exp(2*x)
        b = 14+x**2-x
        c = np.sqrt(b)
        answer = str.format('{0:.3f}', (a/b))
        break

    except ZeroDivisionError:
        print("Error: Denominator equal to 0, try again")
    except:
        print("Error: Please enter a valid number, try again")

print("\nx = ", + x)
print("Operation: (e^2x)/sqrt(14 + x^2 -x)")
print("Result: " + answer)
print("=============================================\n")
