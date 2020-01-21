"""
Homework 1
>Problem 6

Author: Derrick Unger
Date: 1/16/20
CSC232 Winter 2020

"""
import math

a = 2.34 + (9.8*math.log(51))
b = (.5*2.7*(5.9**2 - 2.4**2))

answer = str.format('{0:.4f}', (a+b))
print(answer)
