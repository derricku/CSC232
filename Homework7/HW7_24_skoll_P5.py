"""
Homework 7
>Problem 5
Author: Derrick Unger
Date: 2/29/20
CSC232 Winter 2020
"""

count = 1
last = ["placeholder"]
while True:
    try:
        user = input("Enter a string or 'exit' to quit: ")

        if user.upper() == "EXIT":
            break

        try:
            number = float(user)
            print("Wrong input, try again.")

        except:
            if user[0].upper() == last[count-1].upper() or count == 1:
                last.append(user[len(user) - 1])

                count += 1
            else:
                print("Wrong input, try again.")
    except:
        print("Error. Try again")
