"""
Homework 6
>Problem 5

Author: Derrick Unger
Date: 2/22/20
CSC232 Winter 2020
"""

import time

print("\n" + "="*40)
print("AI - JET BOMBER\n")
print("Instructions: ")
print("When prompted, enter target position, bomb type, and altitude")
print("All entries must be separated by commas.")
print("Position must be an integer between [3 and 49].")
print("Bomb type must be either A or B.")
print("Altitude must be a positive integer")

while True:
    try:
        positionT, bombType, alt = input("\nInput values: ").split(",")

        # Error and Exit Checks
        if positionT.upper() == "EXIT":
            print("\nGame Ended")
            print("="*50 + "\n")
            break
        elif bombType.isnumeric():
            err = 1/0
        elif int(positionT) > 49 or int(positionT) < 3:
            print("Invalid target position.")
        elif bombType.upper() != "A" and bombType.upper() != "B":
            print("Invalid bomb type.")
        elif int(alt) < 0:
            print("Invalid altitude.")

        # Print Game
        else:
            alt = int(alt)
            positionT = int(positionT)

            # Firing Types
            if bombType.upper() == "A":
                if alt % 2 == 0:
                    position = positionT - 1
                else:
                    position = positionT
                print("~"*(position-1), "^", "~"*(50-position))
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
                if alt % 2 == 0:
                    position = positionT + 2
                else:
                    position = positionT - 2
                print("~"*(position-1), "^", "~"*(50-position))
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

            print("~"*(positionT-1), "M", "~"*(50-positionT))
            print("\nEnter exit in the first input to quit... eg 'exit,,'")

    except:
        print("\nError: Invalid input, retry\n")
