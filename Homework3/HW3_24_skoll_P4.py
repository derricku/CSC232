"""
Homework 3
>Problem 4

Author: Derrick Unger
Date: 1/31/20
CSC232 Winter 2020
"""
import numpy as np

# User Input
while True:
    try:
        deg = eval(input("\nInput degree value: "))
        if deg > 360 or deg < -360:
            print("Please input a value between -360 and 360 deg, try again")
        else:
            break
    except:
        print("\nError: Invalid input, retry\n")

# Series Calculation, 10 terms
mySin, mySin2, n = 0, 0, 0
degRad = np.deg2rad(deg)
while n <= 10:
    term = (((-1)**n)*((degRad**(2*n+1))))/np.math.factorial(2*n+1)
    mySin += term
    n += 1

# Special Request, series value when n = 15
n = 15
term = (((-1)**n)*((degRad**(2*n+1))))/np.math.factorial(2*n+1)

# Print Answers, 6 dec accuracy
print("My Series Sin: ", str.format('{0:.6f}', mySin))
print("Numpy Function Sin: ", str.format('{0:.6f}', np.sin(degRad)))
print("Term n = 15: ", str.format('{0:.6f}', mySin2), "\n")
