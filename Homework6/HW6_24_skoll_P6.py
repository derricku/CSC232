"""
Homework 6
>Problem 6

Author: Derrick Unger
Date: 2/22/20
CSC232 Winter 2020
"""

import numpy as np

# BLACKJACK SIM

# Setup Lists
card = []
value = []

# Generate first two cards
np.random.seed(20200222)
randValue = np.random.randint(1, 14, size=100)  # Plenty of Cards
code = 0
cards = 2  # Initial 2 cards
while code == 0:
    total = []  # Reset total
    print("\n  CARD   VALUE")
    for x in range(0, cards):
        if randValue[x] == 1:
            card.append("A")
            total.append(randValue[x])
        
        elif randValue[x] <= 10 and randValue[x] > 1:
            card.append(str(randValue[x]))
            total.append(randValue[x])
    
        elif randValue[x] == 11:
            card.append("J")
            total.append(10)
        elif randValue[x] == 12:
            card.append("Q")
            total.append(10)
        elif randValue[x] == 13:
            card.append("K")
            total.append(10)
        
        # Spacing
        if len(str(card[x])) < 2:
            space1 = "  "
        else:
            space1 = " "
        if len(str(randValue[x])) < 2:
            space = "     "
        else:
            space = "    "
    
        print(space1, card[x], space, total[x])
    print("   Total = ", sum(total))
    
    # Check Against 21
    if sum(total) == 21:
        print("Blackjack!")
        code = 1
    elif sum(total) > 21:
        print("Busted...")
        code = 1
    else:
        # Ask for action
        while True:
            try:
                action = input("\nWant anther card? (YES/NO): ")
                
                if action.upper() != "YES" and action.upper() != "NO":
                    print("Invalid choice, try again...")
                
                elif action.upper() == "YES":
                    print("Yes... your card is: ")
                    cards += 1
                    code = 0
                    break
                    
                elif action.upper() == "NO":
                    print("No... total is: ", sum(total))
                    print("Thanks for playing!")
                    code = 1
                    break
            
            except:
                print("\nError: Invalid input, retry\n")
        
