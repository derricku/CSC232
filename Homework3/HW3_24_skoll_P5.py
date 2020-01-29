"""
Homework 3
>Problem 5

Author: Derrick Unger
Date: 1/31/20
CSC232 Winter 2020
"""

lines = 5
a = 0
s = lines

for n in range(1, lines+1):
    if 2**(n-1) >= 10:
        printLine = "*"
    else:
        printLine = str(2**(n-1))
    x = a
    while x > 0:
        if 2**(x-1) >= 10:
            addedNum = "*"
        else:
            addedNum = str(2**(x-1))
        printLine = addedNum + printLine + addedNum
        x -= 1
    print(" "*s, printLine)
    s -= 1
    a += 1
