"""
Homework 5
>Problem 6

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""
import numpy as np
import matplotlib.pyplot as plt

print("\n")
print("="*50)
print("AI - Rock, Paper, Scissors")
print("="*21)

# PLAYER 2 LEARNS FROM PAST STATISTICAL HISTORY OF WHAT PLAYER 1's RNG CHOOSES
# 1 = Rock, 2 = Paper, 3 = Scissors

p1Wins, p2Wins, tie = 0, 0, 0  # Score Counters
p1Hist1, p1Hist2, p1Hist3 = 0, 0, 0  # Player 1 History Storage
rnd = 0  # Round Counter

# Generate First Round Choice for the AI
np.random.seed(200)
p2Turn = np.random.randint(1, 4)

# Begin Rounds
while rnd < 500:
    # Generate Seed 100 Choice
    np.random.seed(100)
    p1Turn = np.random.randint(1, 4, size=rnd+1)
    p1Turn = p1Turn[rnd]  # Choose latest iteration of array

    # Win Conditions
    if(p1Turn == 1 and p2Turn == 3 or
       p1Turn == 2 and p2Turn == 1 or
       p1Turn == 3 and p2Turn == 2):

        p1Wins += 1

    if(p2Turn == 1 and p1Turn == 3 or
       p2Turn == 2 and p1Turn == 1 or
       p2Turn == 3 and p1Turn == 2):

        p2Wins += 1

    if p1Turn == p2Turn:

        tie += 1

    # Iterate Next Round
    rnd += 1

    # Statistical Analysis for Player 2
    np.random.seed(200)

    if p1Turn == 1:  # Update history storage
        p1Hist1 += 1
    elif p1Turn == 2:
        p1Hist2 += 1
    else:
        p1Hist3 += 1

    if p1Hist1 > p1Hist2 and p1Hist1 > p1Hist3:
        p2Turn = np.random.randint(1, 3, size=rnd+1)  # P2 can't choose paper
        p2Turn = p2Turn[rnd]
        if p2Turn == 2:
            p2Turn = 3

    elif p1Hist2 > p1Hist1 and p1Hist2 > p1Hist3:
        p2Turn = np.random.randint(1, 3, size=rnd+1)  # P2 can't choose scissor
        p2Turn = p2Turn[rnd]

    elif p1Hist3 > p1Hist1 and p1Hist3 > p1Hist2:
        p2Turn = np.random.randint(2, 4, size=rnd+1)  # P2 can't choose rock
        p2Turn = p2Turn[rnd]


# Win Announcement
if p1Wins > p2Wins and tie != rnd:
    print("Seed 100 wins!")
elif p2Wins > p1Wins and tie != rnd:
    print("Seed 200 wins!")
else:
    print("Overall Tie game!!!")

# Results
print("In total:", tie, "games were tied.")
print("Seed 100 won:", p1Wins, "games.")
p1Lossperc = (rnd-tie-p1Wins)/500
p1Winperc = p1Wins/500
tiePerc = tie/500
plt.bar(["Wins", "Losses", "Ties"], [p1Winperc, p1Lossperc, tiePerc])
plt.show()

print("Seed 200 won:", p2Wins, "games.")
p2Lossperc = (rnd-tie-p2Wins)/500
p2Winperc = p2Wins/500
plt.bar(["Wins", "Losses", "Ties"], [p2Winperc, p2Lossperc, tiePerc])
plt.show()

print("\nEven thoguh AI did successfully beat the RNG opponent in this case, "
      "in comparison to Problem 5, the AI actually won less times. In "
      "the purely random case of P5, the win rate of Seed 200 was 35.6%. "
      "Wheras the AI won a lesser 34%  of the time in Problem 6. This test "
      "shows that the AI was not worth the investment to develop. However, "
      "the single test case of two fixed seeds should not be the only "
      "determining factor in this judgement, more testing is required.\n")

print("="*50)
