"""
Homework 5
>Problem 2

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""

import time

sentence = "I am a happy Python learner knowing that a company will hire me"

print(len(sentence))

HowMany = len(sentence)
position = 0
for i in sentence:
    print(i[position], end="")
    time.sleep(.1)

print("\n-----")
