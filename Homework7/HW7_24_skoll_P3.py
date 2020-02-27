"""
Homework 7
>Problem 3
Author: Derrick Unger
Date: 2/29/20
CSC232 Winter 2020
"""

import numpy as np
a = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
count = 0
print("Passwords: ")
while count < 20:
    while True:
        passwrd = []
        for y in range(0, 8):
            passwrd.append(np.random.choice(a))

        # Check for Capitals, Lowers, and Numerics
        if not (any(char.isupper() for char in passwrd)
                and any(char.islower() for char in passwrd)
                and any(char.isnumeric() for char in passwrd)):
            pass
        else:
            count += 1
            break
    print(str(count) + ". " + "".join(passwrd))
