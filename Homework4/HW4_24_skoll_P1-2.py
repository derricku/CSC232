"""
Homework 4
>Problem 1 - P2

Author: Derrick Unger
Date: 2/07/20
CSC232 Winter 2020
"""

inputSum = 0

while True:
    try:
        yourInput = eval(input("Enter a value to add to sum: "))
        inputSum = inputSum + yourInput
        if inputSum > 50:
            break

    except:
        print("Error: Invalid value, continue input\n")

print("\nTotal: ", inputSum)
