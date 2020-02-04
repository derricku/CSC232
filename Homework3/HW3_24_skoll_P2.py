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
        if userInput.upper() == "EXIT":
            print("No longer accepting inputs...")
            code = 1
        else:
            eval(userInput)
            mylist.append(str(userInput))
    except:
        print("Error: wrong value entered")

for n in range(0, len(mylist)):
    print(mylist[n])
print("=============================================\n")
