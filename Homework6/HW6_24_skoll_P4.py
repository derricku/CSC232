"""
Homework 6
>Problem 4

Author: Derrick Unger
Date: 2/22/20
CSC232 Winter 2020
"""

import time

print("\n" + "="*40)
print("JET BOMBER\n")
print("Instructions: ")
print("When prompted, enter jet position, bomb type, and altitude")
print("All entries must be separated by commas.")
print("Position must be an integer between [3 and 49].")
print("Bomb type must be either A or B.")
print("Altitude must be a positive integer")

while True:
    try:
        position, bombType, alt = input("\nInput values: ").split(",")

        # Error and Exit Checks
        if position.upper() == "EXIT":
            print("\nGame Ended")
            print("="*50 + "\n")
            break
        elif bombType.isnumeric():
            err = 1/0
        elif int(position) > 49 or int(position) < 3:
            print("Invalid starting position.")
        elif bombType.upper() != "A" and bombType.upper() != "B":
            print("Invalid bomb type.")
        elif int(alt) < 0:
            print("Invalid altitude.")

        # Print Game
        else:
            position = int(position)
            alt = int(alt)
            print("~"*(position-1), "^", "~"*(50-position))

            # Firing Types
            if bombType.upper() == "A":
                count = 1
                while count < alt+1:
                    if count % 2 == 0:
                        if count % 4 == 0:
                            print(" "*(position-1) + "|")
                        else:
                            print(" "*(position+1) + "|")
                    elif count % 2 != 0:
                        print(" "*(position) + "|")
                    time.sleep(.1)
                    count += 1

            elif bombType.upper() == "B":
                count = 0
                while count < alt:
                    if count % 4 == 0:
                        print(" "*(position-1) + "|")
                    if count % 8 == 1 or count % 8 == 3:
                        print(" "*(position) + "|")
                    if count % 8 == 2:
                        print(" "*(position+1) + "|")
                    if count % 8 == 5 or count % 8 == 7:
                        print(" "*(position-2) + "|")
                    if count % 8 == 6:
                        print(" "*(position-3) + "|")


                    count += 1
                    time.sleep(.1)

            print("~"*25, "\b\b\b", "MMM", "~"*25)
            print("\nEnter exit in the first input to quit... eg 'exit,,'")

    except:
        print("\nError: Invalid input, retry\n")
