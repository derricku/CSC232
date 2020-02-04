"""
Homework 4
>Problem 2

Author: Derrick Unger
Date: 2/07/20
CSC232 Winter 2020
"""

while True:
    try:
        year = input("\nEnter year to judge if leap year or not: ")
        if year == "END":
            break
        year = int(year)
        if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            print("The year is a leap year!")
        else:
            print("The year is NOT a leap year.")

    except:
        print("\nError: Invalid input, retry\n")
