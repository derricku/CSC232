"""
Homework 2
>Problem 4

Author: Derrick Unger
Date: 1/24/20
CSC232 Winter 2020
"""

# Initialize Variables
i = 0  # Array Counter
inputSum = 0

print("\n=======================================")
print("\t   Compound Interest Calculator\n")

while True:
    try:
        yourInput = eval(input("Enter a value to sum up: "))
        inputSum = inputSum + yourInput
        if yourInput == 0:
            break
        i += 1
    except (SyntaxError, NameError, TypeError):
        print("Error: Invalid value, try again\n")

print("\nTotal: ", inputSum)
print("=======================================\n")
