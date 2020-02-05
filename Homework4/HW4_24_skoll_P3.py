"""
Homework 4
>Problem 3

Author: Derrick Unger
Date: 2/07/20
CSC232 Winter 2020
"""
import time

while True:
    try:
        position, type, speed = input("\nInput values: ").split(",")

        # Error and Exit Checks
        if position.upper() == "EXIT":
            print("Game Ended")
            break
        elif type.isnumeric() or speed.isnumeric():
            err = 1/0
        elif int(position) > 40 or int(position) < 0:
            print("Invalid starting position, must be between 0 and 40.")
        elif type.upper() != "A" and type.upper() != "B":
            print("Invalid torpedo type, must be A or B.")
        elif speed.upper() != "N" and speed.upper() != "Z":
            print("Invalid speed type, must be N or Z.")

        # Print Game
        else:
            print("~"*40)
            move = " "*int(position)

            count = 0
            while count < 20:  # Fixed range of 30 requested
                if count % 2 == 0:
                    print(move + "|")
                    count += 1
                    time.sleep(.2)
                else:
                    move += " "
                    count += 1
                    print(move + "|")
                    time.sleep(.2)
            print("~"*35, "\b\b\b", "MMM", "~"*5)
            print("Enter exit in the first input to quit...")

    except ZeroDivisionError:
        print("\nError: Invalid input, retry\n")
