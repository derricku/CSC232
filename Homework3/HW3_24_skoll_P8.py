"""
Homework 3
>Problem 8

Author: Derrick Unger
Date: 1/31/20
CSC232 Winter 2020
"""
import numpy as np

L = [0.25, 1.2, 0.433, 7.0, 0.88, 0.911, 3.157]

print("\nFUNCTION  \tVALUE")
print("========  \t=====")
print("AVG       \t", round(np.average(L), 3))
print("MIN       \t", np.min(L))
print("MAX       \t", np.max(L))
print("MEDIAN    \t", np.median(L))
print("STD       \t", round(np.std(L), 3))
print("VAR       \t", round(np.var(L), 3))
print("PTP       \t", np.ptp(L))
print("PERCENTILE\t", round(np.percentile(L, 3), 3), "\n")
