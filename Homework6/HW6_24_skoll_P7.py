"""
Homework 6
>Problem 7

Author: Derrick Unger
Date: 2/22/20
CSC232 Winter 2020
"""
import numpy as np

np.set_printoptions(formatter={'float_kind': lambda value: format(value, '8.3f'),
                               'int_kind': lambda value: format(value, '10d')})
while True:
    try:
        print("5 Equations, 5 Unkowns Solver")
        print("For equation of form ax^5 + bx^4 + cx^3 + dx^2 + ex = f")
        print("Input coefficients as follows: a b c d e f")
        eqs = []
        for x in range(1, 6):  # 5 Equations
            while True:  # Keep trying same equation input until valid
                try:
                    print("Enter equation ", x, "'s coefficients")
                    a, b, c, d, e, f = input("Coefficients: ").split(" ")
                    eqs.append([float(a), float(b), float(c),
                                float(d), float(e), float(f)])
                    break
                except:
                    print("Error, try inputting that equation again...")

        eqs = np.array(eqs)  # Change list to array
        break

    except:
        print("Error, try again")

try:
    A = np.delete(eqs, 5, 1)
    B = np.linalg.inv(A)
    C = np.array([eqs[0][5], eqs[1][5], eqs[2][5], eqs[3][5], eqs[4][5]])
    ans = np.dot(B, C)

    print(ans)

except:
    print("Invalid equations. Please enter valid set of coefficients.")
