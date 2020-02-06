"""
Homework 4
>Problem 4

Author: Derrick Unger
Date: 2/07/20
CSC232 Winter 2020
"""

import time

print("="*40)
print("\nWW2 SUBMARINE GAME\n")
print("SPECIAL CONDITION: Operates right to left...\n")
print("Instructions: ")
print("When prompted, enter your position, torpedo type, and enemy speed")
print("All entries must be separated by commas.")
print("Position must be an integer between 0 and 40.")
print("NOTE: Position is ditance from right to left now!")
print("Torpedo type must be either A or B.")
print("    -A fires a torpedo that drops two spaces, then moves one space to" \
      " the left.")
print("    -B fires a torpedo that alternates between one and two drops"\
      " then moves one space to the left.")
print("Enemy speed must either be N or Z.")

while True:
    try:
        position, torpedoType, speed = input("\nInput values: ").split(",")

        # Error and Exit Checks
        if position.upper() == "EXIT":
            print("Game Ended")
            print("="*40)
            break
        elif torpedoType.isnumeric() or speed.isnumeric():
            err = 1/0
        elif int(position) > 40 or int(position) < 0:
            print("Invalid starting position, must be between 0 and 40.")
        elif torpedoType.upper() != "A" and torpedoType.upper() != "B":
            print("Invalid torpedo type, must be A or B.")
        elif speed.upper() != "N" and speed.upper() != "Z":
            print("Invalid speed type, must be N or Z.")

        # Print Game
        else:
            print("~"*40)
            move = " "*int(40 - int(position))

            count = 1

            while count <= 20:  # Fixed range of 30 requested

                # Firing Types
                if torpedoType == "A":
                    if count % 2 == 0:
                        print(move + "|")
                        count += 1
                        time.sleep(.1)
                    else:
                        move = " "*int(40 - int(position)-count)
                        count += 1
                        print(move + "|")
                        time.sleep(.1)

                elif torpedoType == "B":
                    if count % 3 == 0:
                        print(move + "|")
                        count += 1
                        time.sleep(.1)
                    else:
                        move = " "*int(40 - int(position)-count)
                        count += 1
                        print(move + "|")
                        time.sleep(.1)

            # Enemy "Speed"
            if speed == "N":
                print("~"*20, "\b\b\b", "MMM", "~"*20, "N SPEED")
            elif speed == "Z":
                print("~"*35, "\b\b\b", "MMM", "~"*5, "Z SPEED")
                
            print("\nEnter exit in the first input to quit... eg 'exit,,'")


    except ZeroDivisionError:

        print("\nError: Invalid input, retry\n")
        
