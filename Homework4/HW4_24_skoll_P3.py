"""
Homework 4
>Problem 3

Author: Derrick Unger
Date: 2/07/20
CSC232 Winter 2020
"""

import time

print("="*40)
print("\nWW2 SUBMARINE GAME\n")
print("Instructions: ")
print("When prompted, enter your position, torpedo type, and enemy speed")
print("All entries must be separated by commas.")
print("Position must be an integer between 0 and 40.")
print("Torpedo type must be either A or B.")
print("    -A fires a torpedo that drops two spaces, then moves one space to" \
      " the right.")
print("    -B fires a torpedo that alternates between one and two drops"\
      " then moves one space to the right.")
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
            move = " "*int(position)
            
            count = 1

            while count <= 20:  # Fixed range of 30 requested
                
                # Firing Types
                if torpedoType == "A":
                    if count % 2 == 0:
                        print(move + "|")
                        count += 1
                        time.sleep(.1)
                    else:
                        move += " "
                        count += 1
                        print(move + "|")
                        time.sleep(.1)

                elif torpedoType == "B":
                    if count % 3 == 0:
                        print(move + "|")
                        count += 1
                        time.sleep(.1)
                    else:
                        move += " "
                        count += 1
                        print(move + "|")
                        time.sleep(.1)
            
            # Enemy "Speed"
            if speed == "N":
                print("~"*20, "\b\b\b", "MMM", "~"*20, "N SPEED")
            elif speed == "Z":
                print("~"*35, "\b\b\b", "MMM", "~"*5, "Z SPEED")
                
            print("\nEnter exit in the first input to quit... eg 'exit,,'")
            
            # Win States
            if (position == "24" or position == "25" or position == "26" and
               torpedoType == "A" and speed == "Z"):
                print("TARGET HIT!")
            elif (position == "20" or position == "21" or position == "22" and 
                 torpedoType == "B" and speed == "Z"):
                print("TARGET HIT!")
            elif (position == "9" or position == "10" or position == "11" and 
                 torpedoType == "A" and speed == "N"):
                print("TARGET HIT!")
            elif (position == "5" or position == "6" or position == "7" and 
                 torpedoType == "B" and speed == "N"):
                print("TARGET HIT!")
            else:
                print("Target Missed...")

    except ZeroDivisionError:

        print("\nError: Invalid input, retry\n")
        
# Win States
# 25 or 24 or 26,A,Z  
# 20 or 21 or 22 ,B,Z
# 9 or 10 or 11, A,N
# 5 or 6 or 7,B,N
