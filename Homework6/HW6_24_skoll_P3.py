"""
Homework 6
>Problem 3

Author: Derrick Unger
Date: 2/22/20
CSC232 Winter 2020
"""

import numpy as np

# Setup Lists
card = []
value = []

# User Input
while True:
    try:
        seed = input("\nInput random generator seed (int) or EXIT to stop: ")

        # Error and Exit Checks
        if seed.upper() == "EXIT":
            print("Exit detected... quitting")
            break

        seed = int(seed)  # Only valid string checked, now int

        if seed < 0:
            print("Seed must be greater or equal to 0!")

        elif seed > 2**32 - 1:
            print("Seed too large. Must be < 2**32 - 1")

        # Generate Random Value
        else:
            np.random.seed(seed)
            # Plenty of replacement values for impossible combinations
            randValue = np.random.randint(1, 14, size=1000)

            code = 0
            while code == 0:  # Keep trying until valid card combo

                print("\n  CARD   VALUE")
                for x in range(0, 5):
                    if randValue[x] == 1:
                        card.append("A")
                    elif randValue[x] <= 10 and randValue[x] > 1:
                        card.append(str(randValue[x]))
                    elif randValue[x] == 11:
                        card.append("J")
                    elif randValue[x] == 12:
                        card.append("Q")
                    elif randValue[x] == 13:
                        card.append("K")

                    # Spacing
                    if len(str(card[x])) < 2:
                        space1 = "  "
                    else:
                        space1 = " "
                    if len(str(randValue[x])) < 2:
                        space = "     "
                    else:
                        space = "    "

                    print(space1, card[x], space, randValue[x])
                print("   Sum = ", np.sum(randValue[0:5]))

                # Check for 5 Same Cards
                iterator = 0
                if str(randValue[0:5]).count(str(randValue[0])) == 5:
                    print("Impossible card combination, changing cards...")
                    iterator = iterator + 5  # Keeps trying new values
                    for n in range(0, 5):
                        randValue[n] = randValue[n + iterator]
                else:
                    code = 1

    except:
        print("\nError: Invalid input, retry\n")
