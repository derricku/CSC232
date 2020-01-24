"""
Homework 2
>Problem 3

Author: Derrick Unger
Date: 1/24/20
CSC232 Winter 2020
"""

# Initialize Variables
i = 0  # Array Counter
inputSum = 0

print("\n=======================================")
print("\t   Input Summer\n")
print("Enter 0 when you are done entering values. \n\n")

while True:
    try:
        yourInput = eval(input("Enter a value to sum up: "))
        inputSum = inputSum + yourInput
        if yourInput == 0:
            break
        i += 1
    except:
        print("Error: Invalid value, continue input\n")

print("\nTotal: ", inputSum)
print("=======================================\n")
