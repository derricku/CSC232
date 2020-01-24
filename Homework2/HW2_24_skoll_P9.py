"""
Homework 2
>Problem 9

Author: Derrick Unger
Date: 1/24/20
CSC232 Winter 2020
"""

import numpy as np

print("\n=======================================")
print("     Half Full Height Calculator\n")


while True:
    try:
        R1 = eval(input("Enter R1 (cm): "))
        R2 = eval(input("Enter R2 (cm): "))
        h1 = eval(input("Enter h (cm): "))

        if R1 < R2:
            print("R1 cannot be smaller than R2, retry\n")
        elif R1 <= 0 or R2 <= 0 or h1 <= 0:
            print("All values must be more than 0, retry\n")
        else:
            break

    except:
        print("\nError: Invalid value, try again\n")

h2 = (h1*R2)/R1  # cm
V1 = np.pi*R1**2*(h1/3)  # mL
V2 = np.pi*R2**2*(h2/3)  # mL
V_cup = V1 - V2  # mL

# Finding the Height at Half Full
V_half = .5*V_cup
V_small = 0
h_half = h1
stepSize = .01

while (h_half > 0) and (V_small <= V_half):
    R3 = ((h_half*(R1 - R2))/h1) + R2
    h3 = (h1*R3)/R1  # cm
    V3 = np.pi*R3**2*(h3/3)  # mL
    V_small = V1 - V3
    h_half -= stepSize

# Interpolation
h_actual = ((h_half + stepSize) + h_half)/2

# Concatenation and Prints
h_actual = str.format('{0:.2f}', h_actual)
V_cup = str.format('{0:.2f}', V_cup)
V_half = str.format('{0:.2f}', V_half)
print("\nVolume of Cup: ", V_cup, "mL")
print("Volume of Cup Half Full: ", V_half, "mL")
print("Height of Etch at Half Full: ", h_actual, "cm")
print("=======================================\n")
