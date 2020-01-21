"""
Homework 1
>Problem 5

Author: Derrick Unger
Date: 1/16/20
CSC232 Winter 2020

"""
import math

a = (14.8**2 + 6.5**2)/(3.8**2)
b = 55/(math.sqrt(2) + 14)

answer = (str.format('{0:.4f}', (a + b)))
print("Answer: ", answer)
