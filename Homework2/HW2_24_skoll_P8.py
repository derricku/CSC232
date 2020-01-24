"""
Homework 2
>Problem 8

Author: Derrick Unger
Date: 1/24/20
CSC232 Winter 2020
"""

import numpy as np

print("\n=======================================")
print("     Cup Volume Calculator\n")


while True:
    try:
        R1 = eval(input("Enter R1 (cm): "))
        R2 = eval(input("Enter R2 (cm): "))
        h = eval(input("Enter h (cm): "))
        break

    except:
        print("\nError: Invalid value, try again\n")

h2 = (h*R2)/R1  # cm
V_larger = np.pi*R1**2*(h/3)  # mL
V_smaller = np.pi*R2**2*(h2/3)  # mL
V_cup = V_larger - V_smaller  # mL
V_cup = str.format('{0:.2f}', V_cup)

print("Volume of Cup in mL", V_cup)
print("=======================================\n")
