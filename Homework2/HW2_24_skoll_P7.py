"""
Homework 2
>Problem 7

Author: Derrick Unger
Date: 1/24/20
CSC232 Winter 2020
"""

# Initialize Variables
i = 0  # Array Counter
inputSum = 0

print("\n=======================================")
print("     Pyramid Volume Calculator\n")


while True:
    try:
        b = eval(input("Enter length of one side of the pyramid base: "))
        h = eval(input("Enter height of the pyramid: "))
        bA = b**2
        V = str.format('{0:.3f}', (1/3)*bA*h)
        break

    except:
        print("\nError: Invalid value, try again\n")

print("Volume of Pyramid is: ", V)
print("=======================================\n")
