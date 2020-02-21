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
        # Angle of Rotation
        print("5 Equations, 5 Unkowns Solver")
        print("For equation of form ax^5 + bx^4 + cx^3 + dx^2 + ex = f")
        print("Input as follows a b c d e f")
        eqs = []
        for x in range(1, 6):  # 5 Equations
            while True:  # Keep trying same equation input until valid
                try:
                    print("Enter equation ", x, "'s coefficients")
                    a, b, c, d, e, f = input("Coeff separated by space: ").split(" ")
                    eqs.append([float(a), float(b), float(c),
                                float(d), float(e), float(f)])
                    break
                except:
                    print("Error, try inputting that equation again...")

        eqs = np.array(eqs)  # Change list to array
        break

    except:
        print("Error, try again.
C = np.array([[eqs[0][5], eqs[0][5], eqs[0][5], eqs[0][5], eqs[0][5]]])
B = np.linalg.inv(A)
ans = np.dot(B, C)

print(ans)
