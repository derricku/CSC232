"""
Homework 3
>Problem 7

Author: Derrick Unger
Date: 1/31/20
CSC232 Winter 2020
"""

# User Input
while True:
    try:
        a, b = input("\nType in two integers eg(1 2): ").split(" ")
        a, b = int(a), int(b)

        sum = a + b

        if sum % 2 == 0:
            print("Sum: ", sum, ", is even\n")
            break
        else:
            print("Sum: ", sum, ", is odd\n")
            break

    except:
        print("\nError: Invalid input, retry\n")
