"""
Homework 5
>Problem 5

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""
import numpy as np
import matplotlib.pyplot as plt

print("\n")
print("="*50)
print("RNG - Rock, Paper, Scissors")
print("="*21)

# BOTH PLAYERS HAVE RNG VALUES, SEEDS ARE FIXED HERE SO SAME OUTCOME RATE
# 1 = Rock, 2 = Paper, 3 = Scissors

p1Wins, p2Wins, tie = 0, 0, 0  # Score Counters
rnd = 0  # Round Counter

np.random.seed(100)
p1Turns = np.random.randint(1, 4, size=[500])  # Same outcome every time
np.random.seed(200)
p2Turns = np.random.randint(1, 4, size=[500])  # since seeds are fixed

# Win and Tie Conditions
while rnd < 500:
    p1Turn = p1Turns[rnd]  # Each array index is another round
    p2Turn = p2Turns[rnd]

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

    rnd += 1  # Next Round

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

print("="*50)
