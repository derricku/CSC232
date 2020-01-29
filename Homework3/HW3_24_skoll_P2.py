"""
Homework 3
>Problem 2
Author: Derrick Unger
Date: 1/31/20
CSC232 Winter 2020
"""

code, i = 0, 0
mylist = []  # Define your list

print("\n=============================================")
while code == 0:
    try:
        userInput = input("Enter a number or type 'EXIT' or 'exit' to stop: ")
        if userInput == "EXIT" or userInput == "exit":
            print("No longer accepting inputs...")
            code = 1
        else:
            mylist.append(eval(userInput))
    except:
        print("Error: wrong value entered")

for i in range(0, len(mylist)):
    for ii in range(0, len(round(max(mylist)))):
        w = 0
    print(mylist[i])
print("=============================================\n")
