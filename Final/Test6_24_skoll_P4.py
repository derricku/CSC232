"""
Test 6
>Problem 4

Author: Derrick Unger
Date: 3/20/20
CSC232 Winter 2020
"""
import time

print("\nPROBLEM 4\n")
print("Instructions: ")
print("When prompted, enter jet position, altitude, and bomb type")
print("**All entries must be separated by commas.")
print("**Position must be an integer between 3 and 70, non-inclusive.")
print("**Altitude must be a positive integer")
print("**Bomb type must be either A or B.")

while True:
    try:
        position, alt, bombType = input("\nInput values: ").split(",")

        # Error and Exit Checks
        if position.upper() == "EXIT":
            print("\nGame Ended")
            print("="*50 + "\n")
            break
        elif bombType.isnumeric():
            err = 1/0
        elif int(position) > 69 or int(position) < 4:
            print("Invalid starting position.")
        elif bombType.upper() != "A" and bombType.upper() != "B":
            print("Invalid bomb type.")
        elif int(alt) < 0:
            print("Invalid altitude.")

        # Print Game
        else:
            position = int(position)
            alt = int(alt)

            # Firing Types
            if bombType.upper() == "A":
                print("~"*(position-1), "^", "~"*(70-position))
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
                print("~"*(position-2), "^", "~"*(70-position))
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

            print("~"*35, "\b\b\b", "MMM", "~"*35)
            print("\nEnter exit in the first input to quit... eg 'exit,,'")

    except:
        print("\nError: Invalid input, retry\n")
