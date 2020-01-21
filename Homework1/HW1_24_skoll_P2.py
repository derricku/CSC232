"""
Homework 1
>Problem 2

Author: Derrick Unger
Date: 1/16/20
CSC232 Winter 2020

"""

# Surface Area Calculation
top = 200*140  # Same area as bottom
topsides = (2*50*140) + (2*50*100)
bottomsides = (2*200*40) + (2*40*140)

SA = 2*top + bottomsides + topsides  # [mm^2] Surface area of 1 fixture

# Volume of Paint Needed
fixtures = 1000  # Number of fixtures
thick = .25*25.4  # [mm] Thickness of paint

paint_vol = SA*thick  # [mm^3] Required volume of paint for fixture Surface
attrition = .4*paint_vol  # [mm^3] Painting Attrition
total_mm = fixtures*(paint_vol+attrition)  # [mm^3]
total_pint = round(total_mm*(2.11338E-6))  # [pint] Convert to Pints & round

print(total_pint, "1-pint cans needed")
