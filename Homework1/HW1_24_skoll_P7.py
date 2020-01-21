"""
Homework 1
>Problem 7

Author: Derrick Unger
Date: 1/16/20
CSC232 Winter 2020

"""
import numpy as np

a = (np.tan(np.deg2rad(64)))/(np.cos(np.deg2rad(14))**2)
b = (3*np.sin(np.deg2rad(80)))/(np.cbrt(.9))
c = (np.cos(np.deg2rad(55)))/(np.sin(np.deg2rad(11)))

answer = str.format('{0:.4f}', (a-b+c))
print(answer)
