"""
Homework 1
>Problem 1

Author: Derrick Unger
Date: 1/16/20
CSC232 Winter 2020

"""
import math  # Faster than np in this case

# Given Variable Definitions
balls = 100  # Number of bowling balls
ball1_diam = 8.5*25.4  # [mm] Unpainted ball diam
ball2_diam = ball1_diam + (2*25.4)  # [mm] Painted ball diam

# Volume of Paint Needed
paint_vol = (4/3)*math.pi*(((ball2_diam/2)**3) - ((ball1_diam/2)**3))  # [mm^3]
attrition = .4*paint_vol  # [mm^3]
total_mm3 = balls*(paint_vol + attrition)  # [mm^3]
total_pint = round(total_mm3*(2.11338E-6))  # [pint] Convert to Pints & round

print(total_pint, "1-pint cans needed")
