"""
Homework 7
>Problem 2
Author: Derrick Unger
Date: 2/29/20
CSC232 Winter 2020
"""

import numpy as np


np.set_printoptions(formatter={'float_kind': lambda value: format(value, '8.3f'),
                               'int_kind': lambda value: format(value, '7d')})

while True:
    try:
        tkts = int(input("\nHow many tickets do you want? "))

        # Check Input Validity
        if tkts < 1:
            print("Must choose an int of 1 or more tickets... try again")

        # Generate Values
        else:
            tkt = np.empty((0, 5), int)
            for x in range(0, tkts):  # Number of tickets to generate
                tktNums = np.array([])

                # Add Values to ticket until all are unique
                code = 0
                while code == 0:
                    randValue = np.random.randint(1, 51)  # Nums [1 to 50]
                    tktNums = np.unique(np.append(tktNums, randValue))
                    if len(tktNums) == 5:  # Do until we have 5 unique values
                        code = 1

                tkt = np.append(tkt, [tktNums], axis=0)  # Add to master list
            break

    except:
        print("Error, invalid input, try again...")


# Print out All Tickets
print("\n\nNumber of tickets: ", tkts)
for x in range(1, len(tkt)+1):
    print("\nTicket " + str(x) + ":")
    print(tkt[x-1])
