"""
Homework 3
>Problem 6

Author: Derrick Unger
Date: 1/31/20
CSC232 Winter 2020
"""

# User Input
while True:
    try:
        a, b, c = input("\nInput three values eg: 1,2,3: ").split(",")
        a, b, c = eval(a), eval(b), eval(c)

        sum = a + b + c
        print("Sum of Values: ", sum)
        print("To quit, input 3 null values separated by commas ',,'")

    except(SyntaxError, NameError):
        if a.strip() + b.strip() + c.strip() == "":
            print("\nExit detected, quitting...\n")
            break
        concat = a.strip() + " " + b.strip() + " " + c.strip()
        print("Concatenation: ", concat)
        print("To quit, input 3 null values separated by commas ',,'")

    except:
        print("\nError: Invalid input, retry\n")
