"""
Homework 5
>Problem 7

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(20200212)
sums = []

for i in range(0, 8000):
    left = np.random.randint(1, 7)
    right = np.random.randint(1, 7)
    sumroll = left + right
    sums.append(sumroll)
    print(left, right)

labels, counts = np.unique(sums, return_counts=True)
plt.xlabel("Number Rolled")
plt.ylabel("Frequency")
plt.title("Sum of Rolled Dice, 8000 Trials")
plt.xlim(1, 13)
plt.xticks(np.arange(2, 13))
plt.bar(labels, counts, align="center")
plt.show()
