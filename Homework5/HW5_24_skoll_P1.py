"""
Homework 5
>Problem 1

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""

import numpy as np

# User Input
while True:
    try:
        seed = int(input("\nInput random generator seed: "))

        if seed < 0:
            print("Seed must be greater or equal to 0!")
        elif seed > 2**32 - 1:
            print("Seed too large. Must be < 2**32 - 1")
        else:
            np.random.seed(seed)
            randValue = np.random.randint(low=-8, high=9, size=18)
            break

    except:
        print("\nError: Invalid input, retry\n")


print("Result:", randValue)
