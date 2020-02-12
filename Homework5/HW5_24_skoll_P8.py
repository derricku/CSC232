"""
Homework 5
>Problem 8

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""

while True:
    try:
        print("\nInstructions: ")
        print("Inputs must be a string of digits, separated by a space.")
        print("Ex: 12345 67890\n")
        s1, s2 = input("\nInput two numeric strings of digits: ").split(" ")

        # Create list of ints from string input
        l1 = list(map(int, list(s1)))
        l2 = list(map(int, list(s2)))

        if len(l1) != len(l2):
            print("String of digits must be the same length! Try again")
        else:
            for i in range(0, len(l1)):
                if l1[i] < l2[i]:
                    l1Temp = l1[i]  # Save original l1 value for swapping
                    l1[i] = l2[i]   # Swap l2 to l1
                    l2[i] = l1Temp  # Assign l2 to old l1 value

                l1[i] = str(l1[i])  # Convert all values back to strings
                l2[i] = str(l2[i])

            # Rejoin list of strings
            s3 = ""
            s4 = ""
            s3 = s3.join(l1)
            s4 = s4.join(l2)

            print("\nOriginal input: ")
            print(s1)
            print(s2)

            print("\nSorted Form: ")
            print(s3)
            print(s4)

            break
    except:
        print("Invalid input, try again")
