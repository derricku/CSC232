"""
Homework 1
>Problem 8

Author: Derrick Unger
Date: 1/16/20
CSC232 Winter 2020

"""

import numpy as np

x = 2.34  # Given

a = np.exp(2*x)
b = np.sqrt(14+x**2-x)

answer = str.format('{0:.4f}', (a/b))
print(answer)
