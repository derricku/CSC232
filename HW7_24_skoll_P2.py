"""
Homework 7
>Problem 2

Author: Derrick Unger
Date: 2/29/20
CSC232 Winter 2020
"""

import numpy as np

while True:
    try:
        tkts = int(input("\nHow many tickets do you want? "))
        
        # Check Input Validity
        if tkts < 1: 
            print("Must choose an int of 1 or more tickets... try again")
        
        # Generate Values
        else:
            tkt = np.array([])
            for x in range(0, tkts):  # Number of tickets to generate
                tktNums = np.array([])
                for y in range(0, 5):  # 5 numbers per ticket
                    code = 0
                    while code == 0:  # Repeat until values are unique
                        randValue = np.random.randint(1, 51)  # Nums [1 to 50]
                        np.append(tktNums, randValue)  # Add value to ticket
                        print(tktNums)
                        # Check for repeats
                        if len(tktNums) == len(set(tktNums)):
                            code = 1
                        else:
                            print("Repeat found, retrying value...")
                print(tktNums)
                np.append(tkt, tktNums)
            break
    
    except ZeroDivisionError:
        print("Error, invalid input, try again...")

"""
# Print out All Tickets
print("Number of tickets: ", tkts)
for x in range(0, tkts):
    print("Ticket ", tkt[x], ":")
    for y in range(0, 5):
        print(tkt[x][y])
"""
